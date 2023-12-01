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
import Footer from "@/components/Footer.vue";

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
    },
    "user_id": parseInt(store.state.auth.user.id) || parseInt(localStorage.getItem("userID")) || 0,
    "status_id": 1
});
// Configuración de la API Key de Google Maps
const center = ref({ lat: -34.397, lng: 150.644 });
const isMapLoaded = ref(false);
const locationConfirmed = ref(false);
// Configuracion multimedia
const showImageInput = ref(false);
const selectedFiles = ref([]);
const fileInput = ref(null);
const isFormLoading = ref(false);

async function uploadImages() {
    if (selectedFiles.value.length > 0 && showImageInput.value) {
        const uploadPromises = selectedFiles.value.map(async file => {
            const formData = new FormData();
            formData.append('file', file);
            formData.append('upload_preset', 'ml_default');

            const response = await fetch('https://api.cloudinary.com/v1_1/dwwer682m/image/upload', {
                method: 'POST',
                body: formData,
            });
            return await response.json();
        });

        try {
            const responses = await Promise.all(uploadPromises);
            responses.forEach(response => {
                newReport.images.push(response.secure_url);
            });
        } catch (error) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'El al subir las imagenes: ' + error
            });
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

    // Variables necesarias para el reporte

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
}

const editLocation = () => locationConfirmed.value = false;

const showImageInputHandler = () => showImageInput.value = showImageInput.value = true;
const hideImageInputHandler = () => showImageInput.value = showImageInput.value = false;
const isNotEmpty = (str) => str.trim().length > 0;
const isLongEnough = (str) => str.trim().length >= MIN_LENGTH;
const containsNonDigitCharacters = (str) => /\D/.test(str);


function handleFiles(event) {
    const files = Array.from(event.target.files).slice(0, 5);
    selectedFiles.value = files;

    if (fileInput.value) {
        fileInput.value.files = createFileList(files);
    }
}

function createFileList(files) {
    const dataTransfer = new DataTransfer();
    files.forEach(file => dataTransfer.items.add(file));
    return dataTransfer.files;
}

async function saveReport() {
    isFormLoading.value = true;
    await uploadImages();
    try {
        const reportCreated = await store.dispatch("reports/createReport", newReport);
        if (reportCreated) {
            Swal.fire({
                icon: 'success',
                title: 'Reporte guardado',
                text: 'El reporte se ha registrado correctamente. Un administrador lo revisará para revisar su veracidad, una vez autorizado su reporte puedes verlo junto a los demás reportes de la página!!'
            });
        }
        router.push({ path: "/reports" });
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: error,
        })
    } finally {
        isFormLoading.value = false;
    }
}

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
                            <div class="option-content" style="color: var(--BgQuaternary);">
                                <ReportIcon :iconValue="category.icon_name" :iconSize="15"
                                    :iconColor="'var(--BgQuaternary)'" />
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
                            class="confirm-position__button btn waves-effect waves-light pulse"
                            style="background-color: var(--BgSecondary);">Confirmar
                            Ubicación</button>
                        <button v-show="locationConfirmed" @click="editLocation"
                            class="confirm-position__button btn waves-effect waves-light"
                            style="background-color: var(--BgSecondary);">Editar
                            Ubicación</button>
                    </div>
                </div>

                <!-- Imagen y videos -->
                <div class="multimedia__container" v-show="!isFormLoading">
                    <div class="shower__container" v-show="!showImageInput">
                        <label for="show-multimedia">¿Tienes fotografías para evidenciar la incidencia? (opcional)</label>
                        <a class="waves-effect waves-light btn-small" style="background-color: var(--BgTertiary);"
                            @click="showImageInputHandler"><i class="material-icons right">drive_folder_upload</i>Subir
                            Evidencia</a>
                    </div>

                    <div class="multimedia-form__container" v-show="showImageInput">
                        <div class="multimedia-input__container">
                            <div class="file-field input-field">
                                <div class="btn" style="background-color: var(--BgQuaternary);">
                                    <span>Evidencia</span>
                                    <input type="file" accept="image/*" multiple @change="handleFiles" ref="fileInput">
                                </div>
                                <div class="file-path-wrapper">
                                    <input class="file-path validate" type="text" placeholder="Sube una o más fotos">
                                </div>
                            </div>
                            <span>
                                <div class="image-counter">
                                    {{ selectedFiles.length }}/5
                                </div>
                            </span>
                        </div>

                        <div class="mutlimedia__buttons">
                            <a @click="hideImageInputHandler" class="btn waves-effect waves-light submit-images__button"
                                style="background-color: var(--red);">Cancelar</a>
                        </div>
                    </div>
                </div>

                <div class="col s12 submit-report__button">
                    <button type="submit" class="btn-large waves-effect waves-light" style="background-color: var(--BgHigher1);"
                        :class="{ 'disabled': !isFormValid || isFormLoading }" @click="saveReport">Enviar Reporte <i
                            class="material-icons right">send</i></button>
                </div>
                <div class="progress" v-show="isFormLoading">
                    <div class="indeterminate"></div>
                </div>
            </div>
        </div>
    </main>
    <Footer />
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
    margin-bottom: 20px;

    button {
        width: 100%;
    }
}

.mutlimedia__buttons {
    margin-top: 10px;
    display: flex;
    justify-content: flex-end;
    gap: 15px;
    align-items: center;

}

.multimedia-input__container {
    display: flex;
    justify-content: flex-start;
    gap: 15px;
    align-items: center;
}
</style>
