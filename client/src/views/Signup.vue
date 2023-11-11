<script setup>
import { onMounted, ref, reactive } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const signupReq = reactive({
  email: '',
  password: '',
  password_confirmation: '',
  username: ''
});

const confirmPassChecker = () => signupReq.password === signupReq.password_confirmation;
const getValidateEmptyFields = () => signupReq.email !== '' || signupReq.password !== '' || signupReq.password_confirmation !== '' || signupReq.username !== '';

const signup = async () => {
  if (!confirmPassChecker()) return;
  if (!getValidateEmptyFields()) return;
  store.dispatch('signup', signupReq);
}

onMounted(() => {
  document.title = 'VC | Registro';
});
</script>


<template>
  <main>
    <img src="../assets/img/Logo Voz Ciudadana.svg" alt="" width="120" height="120">
    <h1>Registrarse</h1>
    <form @submit.prevent @submit="signup">
      <input type="text" name="" placeholder="Usuario" v-model="signupReq.username">
      <input type="email" name="" placeholder="Email" v-model="signupReq.email">
      <input type="password" name="" placeholder="Password" v-model="signupReq.password">
      <input type="password" name="" placeholder="Password" v-model="signupReq.password_confirmation">
      <p v-if="store.state.error !== ''" class="error-message">{{ store.state.error }}</p>
      <input type="submit" value="Registrarme">
    </form>
    <p>Ya tienes cuenta?, <router-link to="/login">Iniciar Sesión</router-link></p>
  </main>
</template>

<style lang="scss" scoped>
main {
  width: 90%;
  display: flex;
  flex-direction: column;
  height: 100vh;
  justify-content: center;
  margin: 0 auto;
}

h1,
p {
  text-align: center;
}

h1 {
  font-size: 3rem;
}

form {
  width: 80%;
  margin: 0 auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

img {
  margin: 0 auto;
}

input[type="submit"] {
  background: #022E40;
  color: #ffffff;
  padding: 10px;
  border-radius: 10px;
  font-size: 1.5rem;
}

.input-text-error {
  color: red;
  border-bottom: 1px solid black;
  box-shadow: 0 1px 0 0 red;
}
</style>