<script setup>
// Imports
import { GoogleMap, Marker } from 'vue3-google-map';
import { ref, watch, onMounted, nextTick, reactive, computed } from 'vue';

// Variables
const props = defineProps({
    showModal: Boolean,
    reportDetails: Object
});
const emit = defineEmits(['update:showModal']);
const mapOptions = reactive({
    center: null,
    zoom: 17
});
const customIcon = ref(null);
const reportHelperVoted = ref(false);
const reportFixedVoted = ref(false);

// Funciones
onMounted(async () => {
    initializeCarousel();
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, { position: "top", inDuration: 250, outDuration: 175, enterDelay: 50, exitDelay: 50 });
});

watch(() => props.showModal, (newVal) => {
    if (!newVal) {
        emit('update:showModal', false);
    }
});

watch(() => props.reportDetails.images, () => {
    initializeCarousel();
}, { deep: true });

watch(() => props.reportDetails, (newVal) => {
    customIcon.value = {
        url: '@/assets/icon/categoriesIcons/no-icon.svg',
    };
    if (newVal && newVal.coords) {
        let lat = parseFloat(newVal.coords.lat);
        let lng = parseFloat(newVal.coords.lng);
        mapOptions.center = { lat, lng };
    }
}, { deep: true, immediate: true });

const closeModal = () => {
    emit('update:showModal', false);
};

const initializeCarousel = () => {
    nextTick(() => {
        var elems = document.querySelectorAll('.carousel');
        var instances = M.Carousel.init(elems, {
            fullWidth: true,
            indicators: true,
            duration: 300,
        });
    });
};

const toggleReportHelperVoted = () => {
    reportHelperVoted.value = !reportHelperVoted.value;
};
const toggleReportFixedVoted = () => {
    reportFixedVoted.value =!reportFixedVoted.value;
};
</script>

<template>
    <transition name="slide-up">
        <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
            <div class="modal-container">
                <div class="modal-header">
                    <button class="close-btn" @click="closeModal">
                        <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink"
                            width="512" height="512" x="0" y="0" viewBox="0 0 512.021 512.021"
                            style="enable-background:new 0 0 512 512" xml:space="preserve" class="">
                            <g>
                                <path
                                    d="M301.258 256.01 502.645 54.645c12.501-12.501 12.501-32.769 0-45.269-12.501-12.501-32.769-12.501-45.269 0L256.01 210.762 54.645 9.376c-12.501-12.501-32.769-12.501-45.269 0s-12.501 32.769 0 45.269L210.762 256.01 9.376 457.376c-12.501 12.501-12.501 32.769 0 45.269s32.769 12.501 45.269 0L256.01 301.258l201.365 201.387c12.501 12.501 32.769 12.501 45.269 0 12.501-12.501 12.501-32.769 0-45.269L301.258 256.01z"
                                    fill="#292929" opacity="1" data-original="#292929"></path>
                            </g>
                        </svg>
                    </button>
                </div>
                <div class="modal-content">
                    <h2>{{ reportDetails.title }}</h2>
                    <p>{{ reportDetails.description }}</p>
                    <div class="report_details">
                        <span class="card-reporter">Por: {{ reportDetails.user.username }}</span>
                        <span class="card-category">{{ reportDetails.category.category_name }}</span>
                    </div>
                    <span class="card-date">{{ new Date(reportDetails.created_at).toLocaleDateString() }}</span>

                    <div class="carousel carousel-slider" v-if="reportDetails.images.length > 0">
                        <a class="carousel-item" v-for="(image, index) in reportDetails.images" :key="index">
                            <img :src="image.image" alt="Report Image">
                        </a>
                    </div>

                    <div class="map-content">
                        <span for="">Ubicación</span>
                        <GoogleMap api-key="AIzaSyAXnAAtV9TCNDfvl9tMx3iwCJC8MCECMCQ" style="width: 100%; height: 300px"
                            :center="mapOptions.center" :zoom="mapOptions.zoom" :streetViewControl="false"
                            :mapTypeControl="false" :fullscreenControl="false">
                            <Marker :options="{ position: mapOptions.center, draggable: false }" :icon="customIcon" />
                        </GoogleMap>
                    </div>

                    <div class="options">
                        <button class="btn tooltipped waves-effect" @click="toggleReportHelperVoted"
                            :style="{ backgroundColor: !reportHelperVoted ? 'white' : '#4cb5ab', color: !reportHelperVoted ? 'black' : 'white' }"
                            :class="{ 'waves-light': reportHelperVoted, 'waves-red': !reportHelperVoted }"
                            data-position="top"
                            :data-tooltip="!reportHelperVoted ? 'Apoyando el reporte 🙌' : 'Dejando de apoyar'"><i
                                class="material-icons">volunteer_activism</i></button>
                        <button class="btn tooltipped waves-effect" @click="toggleReportFixedVoted"
                            :style="{ backgroundColor: !reportFixedVoted ? 'white' : '#f77b72', color: !reportFixedVoted ? 'black' : 'white' }"
                            :class="{ 'waves-light': reportFixedVoted, 'waves-teal': !reportFixedVoted }"
                            data-position="top"
                            :data-tooltip="!reportFixedVoted ? 'Reporte atendido 👍' : 'Sigue sin atender'"><i
                                class="material-icons">construction</i></button>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<style lang="scss" scoped>
.options {
    margin: 30px 0;
    display: flex;
    align-items: center;
    gap: 20px;
    transition: 0.2s ease-in-out;

    button {
        width: 100%;
    }
}


.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    backdrop-filter: blur(15px);
    align-items: flex-end;
    height: 100dvh;
    justify-content: center;
}

.modal-container {
    width: 100%;
    max-width: 500px;
    max-height: calc(100dvh - 150px);
    background-color: #fff;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    overflow-y: auto;
    position: absolute;
    bottom: 0;
    transition: transform 0.3s ease-out;
}

.modal-header {
    display: flex;
    justify-content: flex-end;
    padding: 1rem;
}

.close-btn {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    display: grid;
    place-content: center;
    height: 27px;
    width: 27px;
    border-radius: 5px;
    padding: 7px;

    &:hover {
        background-color: rgba(0, 0, 0, 0.2);
    }

    svg {
        width: 100%;
        height: 100%;
    }
}

.modal-content {
    padding: 1rem;
}

.slide-up-enter-active,
.slide-up-leave-active {
    transition: transform 0.2s ease;
}

.slide-up-enter-from,
.slide-up-leave-to {
    transform: translateY(100%);
}

.slide-up-enter-to,
.slide-up-leave-from {
    transform: translateY(0);
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}

h2 {
    font-size: 2rem;
    font-weight: 500;
}

.card-category {
    top: 20px;
    right: 20px;
    background-color: #0f445b;
    color: #fff;
    padding: 5px 10px;
    border-radius: 2px;
    font-size: 0.8rem;
}

.report_details {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>