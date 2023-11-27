<script setup>
import { useStore } from 'vuex';
import { onMounted, ref, reactive, computed } from 'vue';
import Swal from 'sweetalert2';

// Variables
const store = useStore();
const error = computed(() => store.state.auth.error);
const loginReq = reactive({
  email: '',
  password: ''
})
const inputErrors = reactive({});

// Funciones
onMounted(() => {
  document.title = 'VC | Login';
});
const isLoading = computed(() => store.state.auth.isFormLoading);

const login = async () => {
  handleInputs();
  if (Object.keys(inputErrors).length > 0) {
    return;
  }

  try {
    await store.dispatch('auth/login', loginReq);
  } catch (error) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: error.message
    })
  }
};

const handleInputs = () => {
  const emailRegex = new RegExp("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$");
  const passRegex = new RegExp("^.{8,}$");
  if (loginReq.email === '') {
    inputErrors.email = 'Campo obligatorio';
  } else if (!emailRegex.test(loginReq.email)) {
    inputErrors.email = 'Formato de email incorrecto';
  }

  if (loginReq.password === '') {
    inputErrors.password = 'Campo obligatorio';
  }
};

</script>


<template>
  <main>
    <img src="../assets/img/Logo Voz Ciudadana.svg" alt="" width="120" height="120">
    <h1>Iniciar Sesion</h1>
    <form @submit.prevent @submit="login" novalidate>
      <div class="input-field col s6">
        <i class="material-icons prefix">account_circle</i>
        <input type="email" id="email" class="validate" name="" v-model="loginReq.email"
          @input="store.commit('auth/cleanError');" :class="{ 'invalid': inputErrors.email }">
        <label for="email">Correo electrónico</label>
        <span class="helper-text" :data-error="inputErrors.email" v-show="inputErrors.email"></span>
      </div>

      <div class="input-field col s6">
        <i class="material-icons prefix">key</i>
        <input type="password" name="" id="password" class="validate" :class="{ 'invalid': inputErrors.password }"
          v-model="loginReq.password" @input="store.commit('auth/cleanError');">
        <label for="password">Contraseña</label>
        <span v-show="inputErrors.password" class="helper-text" :data-error="inputErrors.password"></span>
      </div>
      <p v-if="error" class="error-message">{{ error }}</p>
      <input type="submit" value="Iniciar Sesion">
      <div class="progress" v-show="isLoading">
        <div class="indeterminate"></div>
      </div>
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