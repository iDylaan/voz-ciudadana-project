<script setup>
import { onMounted, ref } from 'vue';
import Header from '@/components/Header.vue';
import ProfileThemeEditor from '@/components/ProfileThemeEditor.vue';
import { tokenExpired } from "@/utils/misc.js";

const token = localStorage.getItem('token') ? localStorage.getItem('token') : '';

const authed = ref(!tokenExpired(token));

const firstAccess = ref(false);

onMounted(async () => {
  document.title = 'VC | Home';

  
});



</script>

<template>
  <Header />
  <ProfileThemeEditor first-access="" />
  <main>
    <h1>Bienvenidos</h1>
    <img src="../assets/img/Logo Voz Ciudadana.svg" alt="" width="170" height="170">
    <router-link v-if="!authed" class="btn-start" to="/login">Comenzar</router-link>
    <p>LIFO</p>
  </main>
</template>

<style lang="scss" scoped>
main {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  height: 100vh;
  width: 90%;
  margin: 0 auto;
}

.btn-start {
  background: #022E40;
  color: #ffffff;
  padding: 10px;
  border-radius: 10px;
  font-size: 1.5rem;
  width: 60%;
  margin: 0 auto;
  text-align: center;
}

img {
  margin: 0 auto;
}

h1 {
  text-align: center;
}

@media (width < 350px) {
  h1 {
    font-size: 2rem;
  }
}

p {
  font-weight: lighter;
  letter-spacing: 10px;
  text-align: center;
}
</style>