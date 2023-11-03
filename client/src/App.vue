<template>
  <router-view />
</template>


<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  M.AutoInit();
});
</script>

<style lang="scss">
@import './assets/materialize-src/sass/materialize.scss';
</style>

