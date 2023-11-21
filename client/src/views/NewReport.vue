<script setup>
// Importaciones
import { GoogleMap, Marker } from 'vue3-google-map';
import { ref, onMounted, reactive, nextTick, watch, computed } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Swal from 'sweetalert2';

// Componentes
import Header from "@/components/Header.vue";
import ReportIcon from "@/components/ReportIcon.vue";

// Variables
const MIN_LENGTH = 3;
const isLoadingPage = ref(true);
const isFormValid = computed(() => {
    return (
        isTitleValid.value &&
        isDescriptionValid.value &&
        isCategorySelected.value &&
        isLocationSelected.value &&
        ((showImageInput.value && selectedFiles.value.length > 0) || !showImageInput.value)
    );
});
const isTitleValid = computed(() => isNotEmpty(newReport.title) && isLongEnough(newReport.title) && containsNonDigitCharacters(newReport.title));
const isDescriptionValid = computed(() => isNotEmpty(newReport.description) && isLongEnough(newReport.description) && containsNonDigitCharacters(newReport.description));
const isCategorySelected = computed(() => newReport.category_id > 0);
const isLocationSelected = computed(() => locationConfirmed.value);
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
const locationConfirmed = ref(false);
// Configuracion multimedia
const showImageInput = ref(false);
const selectedFiles = ref([]);
function handleFiles(event) {
    // Limita la cantidad de archivos a 5
    selectedFiles.value = Array.from(event.target.files).slice(0, 5);
}

async function uploadImages() {
    if (selectedFiles.value.length > 0) {
        const formData = new FormData();
        selectedFiles.value.forEach(file => {
            formData.append('file', file);
            formData.append('upload_preset', 'ml_default');
        });
        try {
            const response = await fetch('https://api.cloudinary.com/v1_1/dwwer682m/image/upload', {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error('Error al subir imagen:', error);
        }
    }
}

onMounted(async () => {
    isLoadingPage.value = true;
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
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'El navegador no soporta la geolocalización.'
        });
    }
    isLoadingPage.value = false;
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
    if (!locationConfirmed.value) {
        newReport.coords = event.latLng.toJSON();
    }
}

function updateMarkerPosition(event) {
    newReport.coords = { lat: event.latLng.lat(), lng: event.latLng.lng() };
}

function confirmLocation() {
    locationConfirmed.value = true;
    console.log('Coordenadas seleccionadas:', newReport.coords);
}

const editLocation = () => locationConfirmed.value = false;

const showImageInputHandler = () => showImageInput.value = showImageInput.value = true;
const hideImageInputHandler = () => showImageInput.value = showImageInput.value = false;
const isNotEmpty = (str) => str.trim().length > 0;
const isLongEnough = (str) => str.trim().length >= MIN_LENGTH;
const containsNonDigitCharacters = (str) => /\D/.test(str);
</script>

<template>
    <Header />
    <main class="container">
        <h1 class="center-align">Nuevo Reporte ⚠️</h1>

        <div v-show="isLoadingPage" class="row loader__container">
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

        <div v-show="!isLoadingPage" class="row">
            <div class="col s12">
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
                    <label>Selecciona la ubicación de la incidencia</label>
                    <GoogleMap api-key="AIzaSyAXnAAtV9TCNDfvl9tMx3iwCJC8MCECMCQ" style="width: 100%; height: 500px"
                        :center="center" :zoom="19" @click="updateMarker" :streetViewControl="false" :mapTypeControl="false"
                        :fullscreenControl="false">
                        <Marker :options="{ position: newReport.coords, draggable: !locationConfirmed }"
                            @dragend="updateMarkerPosition" />
                    </GoogleMap>
                    <div class="button__container">
                        <button v-show="!locationConfirmed" @click="confirmLocation"
                            class="confirm-position__button btn waves-effect waves-light blue-grey darken-2">Confirmar
                            Ubicación</button>
                        <button v-show="locationConfirmed" @click="editLocation"
                            class="confirm-position__button btn waves-effect waves-light blue-grey darken-2">Editar
                            Ubicación</button>
                    </div>
                </div>

                <!-- Imagen y videos -->
                <div class="multimedia__container">
                    <div class="shower__container" v-show="!showImageInput">
                        <label for="show-multimedia">¿Tienes fotografías para evidenciar la incidencia? (opcional)</label>
                        <a class="waves-effect waves-light btn-small blue-grey" @click="showImageInputHandler"><i
                                class="material-icons right">drive_folder_upload</i>Subir Evidencia</a>
                    </div>

                    <div class="multimedia-form__container" v-show="showImageInput">
                        <form @submit.prevent="uploadImages">
                            <input type="file" accept="image/*" multiple @change="handleFiles" ref="fileInput">
                            <button type="submit" class="btn waves-effect waves-light" :class="{'disabled': selectedFiles.length === 0}">Subir Imágenes</button>
                        </form>
                    </div>

                </div>

                <div class="col s12 submit-report__button">
                    <button type="submit" class="btn waves-effect waves-light blue"
                        :class="{ 'disabled': !isFormValid }">Enviar Reporte <i
                            class="material-icons right">send</i></button>
                </div>
            </div>
        </div>
    </main>
</template>


<style lang="scss" scoped>
main {
    min-height: 100vh;
    padding: 2rem 0;
    background-color: #fcfcfc;
    width: 100%;

    h1 {
        font-size: 2.5rem;
    }

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

.shower__container {
    display: flex;
    flex-direction: column;
}

.option-content {
    display: flex;
    align-items: center;
    gap: 20px;
}

.loader__container {
    display: grid;
    place-content: center;
    width: 100vw;
}

.map-container {
    margin-top: 280px;
    margin-bottom: 50px;
    height: 500px;
    position: relative;

    label {
        font-size: 1rem;
    }

    .button__container {
        position: absolute;
        bottom: 30px;
        width: calc(100% - 50px);
        display: flex;
        justify-content: center;

        .confirm-position__button {
            width: 70%;
        }
    }
}

.submit-report__button {
    width: 100%;
    margin-top: 20px;

    button {
        width: 100%;
    }
}
</style>
