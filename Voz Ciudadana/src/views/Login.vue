<script setup>
import { useStore } from 'vuex';
import { onMounted, ref, reactive, computed } from 'vue';
import Swal from 'sweetalert2';

// Variables
const store = useStore();
const error = computed(() => store.state.auth.error);
const loginReq = reactive({
  email: {
    value: '',
    valid: false,
    error: null,
    touched: false
  },
  password: {
    value: '',
    valid: false,
    error: null,
    touched: false
  }
})
const validInputs = computed(() => (
  loginReq.email.valid &&
  loginReq.password.valid
));

// Funciones
onMounted(() => {
  document.title = 'VC | Login';
});
const isLoading = computed(() => store.state.auth.isFormLoading);

const login = async () => {
  if (!validInputs) {
    return;
  }

  try {
    await store.dispatch('auth/login', {
      email: loginReq.email.value,
      password: loginReq.password.value
    });
  } catch (error) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: error
    })
  }
};

const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

const validateEmail = () => {
  loginReq.email.touched = true;

  if (loginReq.email.value === '') {
    loginReq.email.valid = false;
    loginReq.email.error = 'El correo electrónico es un campo obligatorio';
    return;
  }

  if (!emailRegex.test(loginReq.email.value)) {
    loginReq.email.valid = false;
    loginReq.email.error = 'Formato de email incorrecto';
    return;
  }

  loginReq.email.valid = true;
  loginReq.email.error = null;
};

const validatePassword = () => {
  loginReq.password.touched = true;

  if (loginReq.password.value === '') {
    loginReq.password.valid = false;
    loginReq.password.error = 'La contraseña es un campo obligatorio';
    return;
  }

  loginReq.password.valid = true;
  loginReq.password.error = null;
};

</script>


<template>
  <main>
    <img src="../assets/img/Logo Voz Ciudadana.svg" alt="" width="120" height="120">
    <h1>Iniciar Sesion</h1>
    <form @submit.prevent novalidate @submit="login">
      <div class="input-field col s6">
        <i class="material-icons prefix">account_circle</i>
        <input type="email" id="email" name="" v-model.trim="loginReq.email.value" @blur="validateEmail"
          @input="store.commit('auth/cleanError');"
          :class="{ 'invalid': loginReq.email.touched ? !loginReq.email.valid : false }">
        <label for="email">Correo electrónico</label>
        <span class="helper-text" :data-error="loginReq.email.error" v-show="loginReq.email.error"></span>
      </div>

      <div class="input-field col s6">
        <i class="material-icons prefix">key</i>
        <input type="password" name="" id="password" @change="validatePassword"
          :class="{ 'invalid': loginReq.password.touched ? !loginReq.password.valid : false }"
          v-model.trim="loginReq.password.value" @input="store.commit('auth/cleanError');">
        <label for="password">Contraseña</label>
        <span v-show="loginReq.password.error" class="helper-text" :data-error="loginReq.password.error"></span>
      </div>
      <p v-if="error" class="error-message">{{ error }}</p>
      <button type="submit" class="waves-effect waves-light btn-large" :class="{ 'disabled': !validInputs }">Iniciar
        Sesión</button>
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

.btn-large {
  background-color: var(--BgSecondary);
  color: white;
}
</style>