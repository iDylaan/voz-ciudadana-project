<script setup>
// Importaciones
import { ref, onMounted, reactive, computed, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Swal from 'sweetalert2';

// Componentes
import Header from "@/components/Header.vue";
import ReportDetails from "@/components/ReportDetails.vue";
import Footer from '@/components/Footer.vue';

// Variables
const router = useRouter();
const store = useStore();
const reports = ref([]);
const searchQuery = ref('');
const sortOption = ref('recent');
const groupOption = ref('all');
const limit = ref(10); // Número inicial de reportes a mostrar
const isLoadingPage = ref(true);
const isModalOpen = ref(false);
let selectedReport = {};

// Funciones
onMounted(async () => {
  isLoadingPage.value = true;
  await updateReports();
  createIntersectionObserver();
  isLoadingPage.value = false;
});

const showModal = (report) => {
  selectedReport = report;
  isModalOpen.value = true;
}

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
};

const groupedReports = computed(() => {
  const now = new Date();
  const periods = {
    'today': d => d.toDateString() === now.toDateString(),
    'week': d => d > new Date(now.setDate(now.getDate() - 7)),
    'month': d => d.getMonth() === now.getMonth(),
    '3months': d => d > new Date(now.setMonth(now.getMonth() - 3)),
    'year': d => d.getFullYear() === now.getFullYear(),
    'all': () => true
  };

  return reports.value.filter(report => {
    const reportDate = new Date(report.created_at);
    return periods[groupOption.value](reportDate);
  });
});

const sortedAndFilteredReports = computed(() => {
  let filtered = groupedReports.value.filter(report =>
    report.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    report.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    report.user.username.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    report.category.category_name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );

  if (sortOption.value === 'recent') {
    filtered.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
  } else if (sortOption.value === 'oldest') {
    filtered.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
  }

  return filtered;
});

const displayedReports = computed(() => {
  return sortedAndFilteredReports.value.slice(0, limit.value);
});

const loadMoreReports = () => {
  limit.value += 10; // Cargar 10 reportes más
};

const createIntersectionObserver = () => {
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      loadMoreReports();
    }
  }, { threshold: 1.0 });

  observer.observe(document.querySelector('#loadMoreMarker'));
};
</script>

<template>
  <Header />

  <main class="container">
    <h1 class="center-align">Reportes Recientes</h1>

    <!-- Búsqueda y Opciones de Filtrado -->
    <div class="row">
      <div class="input-field col s12 m6">
        <i class="material-icons prefix">search</i>
        <input type="text" id="search" v-model="searchQuery">
        <label for="search">Buscar Reportes</label>
      </div>
      <div class="input-field col s12 m6">
        <select v-model="sortOption" class="browser-default">
          <option value="recent">Más Recientes</option>
          <option value="oldest">Más Antiguos</option>
        </select>
      </div>
    </div>

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

    <!-- Lista de Reportes -->
    <div class="row" v-show="!isLoadingPage">
      <div v-for="report in displayedReports" :key="report.id" class="col s12 m6 l4 xl3">
        <div class="card report-card">
          <div class="card-content">
            <span class="card-category">{{ report.category.category_name }}</span>
            <div class="report_details">
              <span class="card-date">{{ new Date(report.created_at).toLocaleDateString() }}</span>
              <span class="card-reporter">Por: <span style="color: var(--BgQuaternary);">{{ report.user.username }}</span></span>
            </div>
            <span class="card-title">{{ report.title }}</span>
            <p class="card-description">{{ report.description }}</p>
            <div class="card-image">
              <img v-if="report.images.length > 0" :src="report.images[0].image" alt="Imagen del Reporte">
              <i v-else class="material-icons">image</i>
            </div>
          </div>
          <div class="card-action">
            <a style="color: var(--BgSecondary);" @click="showModal(report)">Ver Detalles</a>
          </div>
        </div>
      </div>


      <div v-show="displayedReports.length > limit" id="loadMoreMarker" class="col s12 center-align">
        <a class="waves-effect waves-light btn">Cargar más</a>
      </div>
    </div>

    <ReportDetails :show-modal="isModalOpen" :report-details="selectedReport"
      @update:showModal="isModalOpen = $event" />
  </main>
  <Footer />
</template>


<style lang="scss" scoped>
main {
  min-height: 100vh;
  padding: 2rem 0;
  background-color: #fcfcfc;
  width: 100%;
  margin-top: 40px;

  h1 {
    font-size: 2.2rem;
  }

  .card.report-card {
    position: relative;
    background-color: white;
    border-radius: 4px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);

    .card-content {
      position: relative;
      color: #424242;
      padding: 20px;

      .card-category {
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: var(--BgTertiary);
        color: #fff;
        padding: 5px 10px;
        border-radius: 2px;
        font-size: 0.8rem;
      }

      .report_details {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 10px;
        max-width: calc(100% - 56px);
      }

      .card-date {
        font-size: 0.9rem;
        color: #9e9e9e;
      }

      .card-reporter {
        font-size: 0.9rem;
        color: #9e9e9e;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      .card-title {
        font-size: 1.4rem;
        font-weight: bold;
        margin-top: 10px;
      }

      .card-description {
        font-size: 0.9rem;
        line-height: 1.5;
        color: #616161;
        height: 3em; // Limit description height
        overflow: hidden;
        text-overflow: ellipsis;
      }

      .card-image {
        height: 200px;
        margin-top: 15px;
        background-color: #f5f5f5;
        display: flex;
        justify-content: center;
        align-items: center;

        img {
          max-height: 100%;
          max-width: 100%;
          object-fit: cover;
          object-position: center;
        }

        .material-icons {
          font-size: 4rem;
          color: #9e9e9e;
        }
      }

    }

    .card-action {
      border-top: 1px solid #eeeeee;
      padding: 10px 20px;

      a {
        color: #039be5;
        text-transform: uppercase;
        font-weight: bold;
        cursor: pointer;
      }
    }
  }
}

.loader__container {
  display: grid;
  place-content: center;
  width: 100vw;
}
</style>