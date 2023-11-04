<script setup>
import { onMounted, ref } from 'vue';
import Header from '@/components/Header.vue';


onMounted(() => {
  document.title = 'VC | Home';
});

</script>

<template>
  <div class="home view-content">
    <Header />
    <router-link to="/login">Iniciar Sesión</router-link>
  </div>
</template>

<style lang="scss" scoped></style>