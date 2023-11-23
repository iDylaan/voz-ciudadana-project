

<script setup>
import { useStore } from 'vuex';
import { onMounted, ref, reactive, computed } from 'vue';

const store = useStore();
const error = computed(() => store.state.auth.error);
const loginReq = reactive({
  email: '',
  password: ''
})
onMounted(() => {
  document.title = 'VC | Login';
});

const getValidateEmptyFields = () => loginReq.email !== '' || loginReq.password !== '';


const login = async () => {
  if (!getValidateEmptyFields()) return;
  await store.dispatch('auth/login', loginReq);
};

</script>


<template>
  <main>
    <img src="../assets/img/Logo Voz Ciudadana.svg" alt="" width="120" height="120">
    <h1>Iniciar Sesion</h1>
    <form @submit.prevent @submit="login">
      <input type="email" name="" placeholder="Email" v-model="loginReq.email" @input="store.commit('auth/cleanError');">
      <input type="password" name="" placeholder="Password" v-model="loginReq.password"
        @input="store.commit('auth/cleanError');">
      <p v-if="error" class="error-message">{{ error }}</p>
      <input type="submit" value="Iniciar Sesion">
    </form>
    <p>No tienes cuenta?, <router-link to="/signup">Registrate</router-link></p>
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

.error-message {
  padding: 10px;
  color: white;
  background-color: rgb(253, 71, 71);
  border: 1px solid rgb(135, 0, 0);
}
</style>