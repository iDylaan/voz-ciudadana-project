<script setup>
import { onMounted, ref } from 'vue';

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
  </div>
</template>