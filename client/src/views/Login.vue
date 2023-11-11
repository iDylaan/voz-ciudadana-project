

<script setup>
import { onMounted, ref } from 'vue';
import Header from '../components/Header.vue'

onMounted(() => {
  document.title = 'VC | Login';

});

</script>


<template>
  <main>
    <img src="../assets/img/Logo Voz Ciudadana.svg" alt="" width="120" height="120">
    <h1>Iniciar Sesion</h1>
    <form action="">
      <input type="text" name="" id="" placeholder="Email">
      <input type="text" name="" id="" placeholder="Password">
      <input type="submit" value="Iniciar Sesion">
    </form>
    <p>No tienes cuenta?, <router-link to="/signup">Registrate</router-link></p>
  </main>
</template>

<style lang="scss" scoped>
main{
  width: 90%;
  display: flex;
  flex-direction: column;
  height: 100vh;
  justify-content: center;
  margin: 0 auto;
}
h1, p{
  text-align: center;
}

h1{
  font-size: 3rem;
}

form{
  width: 80%;
  margin: 0 auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
img{
  margin: 0 auto;
}

input[type = "submit"]{
  background: #022E40;
  color: #ffffff;
  padding: 10px;
  border-radius: 10px;
  font-size: 1.5rem;
}
</style>