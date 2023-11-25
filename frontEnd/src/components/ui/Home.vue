<script setup>
import Header from '@/components/ui/Header.vue';
import logo from '@/img/logo.svg'

const imgLogo = logo

</script>

<template>
  <Header />
  <main>
    <h1>Bienvenidos</h1>
    <img :src='imgLogo.src' alt="" width="170" height="170">
    <button class="btn-start" to="/login">Comenzar</button>
    <p>LIFO</p>
  </main>
</template>

<style lang="css" scoped>
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