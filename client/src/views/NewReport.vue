<script setup>
// Importaciones
import { useLoadScript, GoogleMap, Marker } from 'vue3-google-map';
import { ref, onMounted, reactive, nextTick, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Swal from 'sweetalert2';

// Componentes
import Header from "@/components/Header.vue";
import ReportIcon from "@/components/ReportIcon.vue";

// Variables
const reportCategories = ref([]);
const store = useStore();
const router = useRouter();
const newReport = reactive({
    "title": "",
    "description": "",
    "category_id": 0,
    "images": [],
    "coords": {
        "lat": -34.397,
        "lng": 150.644
    }
});
// Configuración de la API Key de Google Maps
const center = ref({ lat: -34.397, lng: 150.644 });
const isMapLoaded = ref(false);

onMounted(async () => {
    isMapLoaded.value = false;
    await getReportCategories();

    // Asegúrate de que Materialize CSS haya sido cargado correctamente.
    nextTick(() => {
        var elems = document.querySelectorAll('select');
        M.FormSelect.init(elems);
    });

    // Configuración de Google Maps Ubicación actual
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                center.value = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                newReport.coords = center.value;
                isMapLoaded.value = true;
            },
            () => { },
            { enableHighAccuracy: true }
        );
    }
});

// Observa cambios en reportCategories y actualiza el componente de selección de Materialize
watch(reportCategories, () => {
    nextTick(() => {
        var elems = document.querySelectorAll('select');
        M.FormSelect.init(elems);
    });
});

async function getReportCategories() {
    try {
        await store.dispatch("reports/getReportCategories");
        reportCategories.value = store.state.reports.reports.reportCategories;
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: error,
        })
    }
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}


function updateMarker(event) {
    newReport.coords = event.latLng.toJSON();
}

function updateMarkerPosition(event) {
    newReport.coords = { lat: event.latLng.lat(), lng: event.latLng.lng() };
}

function confirmLocation() {
    // Aquí puedes manejar las coordenadas seleccionadas
    console.log('Coordenadas seleccionadas:', newReport.coords);
}
</script>

<template>
    <Header />
    <main class="container">
        <h1 class="center-align">Nuevo Reporte ⚠️</h1>

        <div class="row">
            <form @submit.prevent="submitReport" class="col s12">
                <div class="input-field col s12">
                    <input id="report_title" type="text" v-model="newReport.title" required>
                    <label for="report_title">Título del Reporte</label>
                </div>
                <div class="input-field col s12">
                    <textarea id="report_description" class="materialize-textarea" v-model="newReport.description"
                        required></textarea>
                    <label for="report_description">Descripción</label>
                </div>
                <div class="input-field col s12">
                    <select id="report_category" v-model="newReport.category_id" required>
                        <option value="" disabled selected>Elige una categoría</option>
                        <option class="report-category-option" v-for="(category, index) in reportCategories"
                            :key="category.id" :value="category.id">
                            <div class="option-content">
                                <ReportIcon :iconValue="category.icon_name" :iconSize="15" :iconColor="'#26a69a'" />
                                {{ capitalize(category.category_name) }}
                            </div>
                        </option>
                    </select>
                    <label for="report_category">Categoría</label>
                </div>

                <!-- Goole Map -->
                <div v-if="isMapLoaded" class="map-container">
                    <GoogleMap api-key="AIzaSyAXnAAtV9TCNDfvl9tMx3iwCJC8MCECMCQ" style="width: 100%; height: 500px"
                        :center="center" :zoom="15" @click="updateMarker">
                        <Marker :options="{ position: markerPosition, draggable: true }" @dragend="updateMarkerPosition" />
                    </GoogleMap>
                    <button @click="confirmLocation">Confirmar Ubicación</button>
                </div>

                <div class="col s12">
                    <button type="submit" class="btn waves-effect waves-light">Enviar Reporte</button>
                </div>
            </form>
        </div>
    </main>
</template>


<style lang="scss" scoped>
main {
    min-height: 100vh;
    padding: 2rem 0;
    background-color: #fcfcfc;
    width: 100%;

    .form {
        margin-top: 2rem;

        form {
            padding: 0 2rem;

            .input-field {
                margin-bottom: 1.5rem;
            }

            button {
                width: 100%;
                margin-top: 1rem;
            }
        }
    }
}

.option-content {
    display: flex;
    align-items: center;
    gap: 20px;
}

.map-container {
    height: 300px;
}
</style>
