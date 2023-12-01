<script setup>
// Importaciones
import { onMounted, ref } from 'vue';
import { GoogleMap, Marker } from 'vue3-google-map';
import { useStore } from 'vuex';
import Swal from 'sweetalert2';

// Componentes
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import ReportDetails from "@/components/ReportDetails.vue";

// Variables
const isLoading = ref(false);
const store = useStore();
const reports = ref([]);
let selectedReport = {};
const center = ref({ lat: -34.397, lng: 150.644 });
const mapStyles = ref([
    {
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#f5f5f5"
            }
        ]
    },
    {
        "elementType": "labels.icon",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#616161"
            }
        ]
    },
    {
        "elementType": "labels.text.stroke",
        "stylers": [
            {
                "color": "#f5f5f5"
            }
        ]
    },
    {
        "featureType": "administrative.land_parcel",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#bdbdbd"
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#eeeeee"
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#757575"
            }
        ]
    },
    {
        "featureType": "poi.park",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#e5e5e5"
            }
        ]
    },
    {
        "featureType": "poi.park",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#9e9e9e"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#ffffff"
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#757575"
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#dadada"
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#616161"
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#9e9e9e"
            }
        ]
    },
    {
        "featureType": "transit.line",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#e5e5e5"
            }
        ]
    },
    {
        "featureType": "transit.station",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#eeeeee"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#c9c9c9"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#9e9e9e"
            }
        ]
    }
]);
const isModalOpen = ref(false);

// Funciones reservadas
onMounted(async () => {
    isLoading.value = true;

    // Configuración de Google Maps Ubicación actual
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                center.value = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
            },
            () => { },
            { enableHighAccuracy: true }
        );
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'El navegador no soporta la geolocalización.'
        });
    }


    try {
        await updateReports();
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Hubo un error al obtener los reportes.'
        });
    }

    isLoading.value = false;
});

// Funciones
const updateReports = async () => {
    try {
        await store.dispatch("reports/getReports");
        reports.value = store.state.reports.reports.reports;
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: error,
        })
    }
    console.log(reports.value);
};


const getIconPath = (iconName) => {
    return require(`@/assets/icon/categoriesIcons/${iconName}.svg`);
};

const showModal = (report) => {
    selectedReport = report;
    isModalOpen.value = true;
};
</script>

<template>
    <div>
        <Header />
        <main>
            <h1>Mapa de reportes🌎</h1>

            <div class="loader" v-show="isLoading">
                <div class="preloader-wrapper big active">
                    <div class="spinner-layer spinner-blue-only">
                        <div class="circle-clipper left">
                            <div class="circle"></div>
                        </div>
                        <div class="gap-patch">
                            <div class="circle"></div>
                        </div>
                        <div class="circle-clipper right">
                            <div class="circle"></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="map__container" v-if="!isLoading">
                <GoogleMap api-key="AIzaSyAXnAAtV9TCNDfvl9tMx3iwCJC8MCECMCQ"
                    style="width: 100%; height: calc(100dvh - 150px)" :center="center" :zoom="17" :streetViewControl="false"
                    :mapTypeControl="false" :fullscreenControl="false" :styles="mapStyles" map-type-id="roadmap">
                    <Marker :options="{
                        position: center, icon: {
                            url: require(`@/assets/icon/categoriesIcons/location.svg`),
                            scaledSize: { width: 35, height: 35 },
                        }
                    }" />
                    <Marker v-for="(report, index) in reports" :key="index" :options="{
                        position: {
                            lat: parseFloat(report.coords.lat),
                            lng: parseFloat(report.coords.lng)
                        },
                        icon: {
                            url: getIconPath(report.category.icon_name),
                            scaledSize: {
                                width: 30,
                                height: 30
                            }
                        },
                    }" @click="showModal(report)" />
                </GoogleMap>
            </div>
            <ReportDetails :show-modal="isModalOpen" :report-details="selectedReport"
                @update:showModal="isModalOpen = $event" />
        </main>
        <Footer />
    </div>
</template>

<style lang="scss" scoped>
main {
    margin-top: 80px;
    min-height: 100dvh;

    h1 {
        width: calc(100vw - 20px);
        font-size: 2rem;
        margin: 0 auto;
        padding-bottom: 10px;
    }
}

.map__container {
    width: calc(100vw - 20px);
    margin: auto;
    margin-bottom: 20px;
}

.loader {
    width: 100vw;
    display: grid;
    place-content: center;
}
</style>
