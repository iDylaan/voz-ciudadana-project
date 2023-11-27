<script setup>
// Importaciones
import { onMounted, ref, nextTick, watchEffect, computed } from "vue";
import Swal from 'sweetalert2';
import { useStore } from "vuex";

// Componentes
import Header from '@/components/Header.vue';

// Variables
const reports = ref([]);
const store = useStore();
const isLoading = ref(false);

// Funciones
onMounted(async () => {
    await updateReports();
});

watchEffect(() => {
    if (reports.value.length) {
        nextTick(() => {
            try {
                let elements = document.querySelectorAll('.carousel');
                M.Carousel.init(elements, {
                    fullWidth: true,
                    indicators: true
                });
            } catch (error) {
            }
        });
    }
});

const updateReports = async () => {
    isLoading.value = true;
    try {
        reports.value = await store.dispatch("reports/getPendingReports");

        reports.value.forEach((report) => {
            report.created_at = new Date(report.created_at).toLocaleDateString();
            report.last_update = new Date(report.last_update).toLocaleDateString();
        });
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: error,
        })
    } finally {
        isLoading.value = false;
    }
};

const declinateReport = async (report) => {
    try {
        await store.dispatch("reports/declinateReport", report);
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: error,
        })
    } finally {
        await updateReports();
    }
};
const activateReport = async (report) => {
    try {
        await store.dispatch("reports/activateReport", report);
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: error,
        })
    } finally {
        await updateReports();
    }
};

</script>

<template>
    <div>
        <Header />
        <main>
            <h1>Admin Home</h1>

            <h3>Reportes Pendientes</h3>

            <div class="loader__container" v-show="isLoading">
                <div class="preloader-wrapper big active loader">
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

            <div class="table__container" v-show="!isLoading">
                <table class="centered striped">
                    <thead>
                        <tr class="cab">
                            <th class="thead-content">Id</th>
                            <th class="thead-content th-left">Titulo</th>
                            <th class="thead-content th-left">Descripción</th>
                            <th class="thead-content th-left">Usuario</th>
                            <th class="thead-content th-right">Fecha de creación</th>
                            <th class="thead-content th-right">Última actualizción</th>
                            <th class="thead-content th-category">Categoría</th>
                            <th class="thead-content">Imágenes</th>
                            <th class="thead-content">Opciones</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="(report, index) in reports" :key="index">
                            <td>{{ report.id }}</td>
                            <td class="th-left">
                                <div class="tbody-content title">{{ report.title }}</div>
                            </td>
                            <td class="th-left">
                                <div class="tbody-content description">{{ report.description }}</div>
                            </td>
                            <td class="th-left">
                                <div class="tbody-content">{{ report.user.username }}</div>
                            </td>
                            <td class="th-right">
                                <div class="tbody-content">{{ report.created_at }}</div>
                            </td>
                            <td class="th-right">
                                <div class="tbody-content">{{ report.last_update }}</div>
                            </td>
                            <td>
                                <div class="tbody-content"><span class="category-ticket">{{ report.category.category_name
                                }}</span></div>
                            </td>
                            <td class="images-content">
                                <div class="tbody-content">
                                    <div class="carousel carousel-slider">
                                        <a class="carousel-item" v-for="(image, index) in report.images"
                                            :key="index">
                                            <img :src="image.image" alt="Imagen del reporte">
                                        </a>
                                        <a class="carousel-item" v-if="report.images.length === 0">
                                            <i class="material-icons">image</i>
                                        </a>
                                    </div>
                                </div>
                            </td>
                            <td class="imgs__container">
                                <div class="tbody-content row-options">
                                    <button @click="declinateReport(report.id)" class="waves-effect waves-light btn"><i
                                            class="material-icons">cancel</i></button>
                                    <button @click="activateReport(report.id)" class="waves-effect waves-light btn"><i
                                            class="material-icons">check_circle</i></button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </main>
    </div>
</template>

<style lang="scss" scoped>
main {
    margin-top: 100px;
}
.loader__container {
    width: 100vw;
    margin: auto;
    display: grid;
    place-content: center;
    padding: 40px 0px;
}
.images-content {
    width: 200px;
}

.carousel {
    height: 300px; // Ajusta esto según tus necesidades
    width: 200px;
    display: grid;
    margin-top: -100px;

    .carousel-item {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;

        img {
            height: 200px;
            width: 200px;
            object-fit: cover;
        }
    }
}



.title {
    min-width: 150px;
}

.description {
    min-width: 200px;
}

.table__container {
    width: calc(100dvw - 10px);
    margin: auto;
    overflow-x: auto;
}

@media (width > 700px) {
    .table__container {
        width: calc(100dvw - 50px);
        margin: auto;
    }

    h3 {
        margin-left: 25px;
    }
}

@media (width > 100px) {
    .table__container {
        width: 90%;
        margin: auto;
    }

    h3 {
        margin-left: 10%;
    }
}

td {
    border: 1px solid rgba(128, 128, 128, 0.226);
    flex-wrap: nowrap;
    max-height: 20px;
}

.waves-light {
    background-color: #0F445B;
}

.cab {
    background-color: #0F445B;
}

h1 {
    text-align: center;
}

body {
    display: flexbox;
}

.opt {
    width: 120px;
}

h3 {
    font-size: 2rem;
    margin-left: 5px;
}

h1 {
    font-size: 2.5rem;
    color: rgba(3, 26, 36, 0.788);
}

.thead-content {
    color: white;
}

.category-ticket {
    background-color: #90c7d8;
    color: #275e6d;
    padding: 7px;
    border-radius: 50px;
    font-size: 0.7rem;
    font-weight: bold;
}

.th-category {
    min-width: 130px;
}

.th-left {
    text-align: left;
}

.th-right {
    text-align: right;
}

.row-options {
    display: flex;
    gap: 10px;
    justify-content: center;
    align-items: center;
}
</style>