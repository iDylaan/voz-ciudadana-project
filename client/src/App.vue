<template>
  <router-view />
  <Navbar />
</template>


<script setup>
import { onMounted } from 'vue';
import Navbar from '@/components/Navbar.vue';

onMounted(() => {
  M.AutoInit();
});
</script>

<style lang="scss">
@import './assets/materialize-src/sass/materialize.scss';
</style>

