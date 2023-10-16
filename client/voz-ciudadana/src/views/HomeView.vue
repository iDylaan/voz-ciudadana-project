<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const reports = ref([]);

onMounted(async () => {
  try {
    const respose = await axios({
      method: 'GET',
      url: 'http://localhost:5000/reports'
    })

    const result = respose.data;
    const data = result.data;
    data.forEach(report => {
      reports.value.push(report);
      console.log(report);
    });
  } catch (error) {
    console.log(error);
  }
});

</script>


<template>
  <div class="home">
    <h1>Consulta de Reportes</h1>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Titulo</th>
          <th>Descripcion</th>
          <th>Categoria</th>
          <th>Ultima actualizacion</th>
          <th>Creado</th>
          <th>Imagenes</th>
          <th>Publicado por</th>
          <th>Estado</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(report, index) in reports" :key="index">
          <td>{{ report.id }}</td>
          <td>{{ report.title }}</td>
          <td>{{ report.description }}</td>
          <td>{{ report.category.category_name }}</td>
          <td>{{ report.last_update }}</td>
          <td>{{ report.created_at }}</td>
          <td>
            <div class="report_images">
              <span v-if="report.images.length === 0">Sin imagenes</span>
              <img v-for="(image, index) in report.images" :key="index" :src="image" />
            </div>
          </td>
          <td>{{ report.user.username }}</td>
          <td>{{ report.status.status_name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style lang="scss">
</style>