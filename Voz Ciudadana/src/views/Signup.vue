<script setup>
import { onMounted, ref, reactive, computed } from 'vue';
import { useStore } from 'vuex';
import Swal from 'sweetalert2';

const store = useStore();
const inputs = ['email', 'password', 'password_confirmation', 'username'];
const signupReq = reactive({
  email: '',
  password: '',
  password_confirmation: '',
  username: ''
});
const inputErrors = ref({});
const isLoading = computed(() => store.state.auth.isFormLoading);

const signup = async () => {
  handleInputs();
  console.log(inputErrors.value);
  if (Object.keys(inputErrors.value).length > 0) {
    return;
  }

  try {
    await store.dispatch('auth/signup', signupReq);
  } catch (error) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: error.message
    })
  }
}

const handleInputs = () => {
  inputErrors.value = {};
  const emailRegex = new RegExp("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$");
  const passRegex = new RegExp("^.{8,}$");

  if (signupReq.username === '') {
    inputErrors.value.username = 'Campo obligatorio';
  } else if (signupReq.username.length < 4) {
    inputErrors.value.username = 'El nombre de usuario debe tener al menos 4 caracteres';
  }

  if (signupReq.email === '') {
    inputErrors.value.email = 'Campo obligatorio';
  } else if (!emailRegex.test(signupReq.email)) {
    inputErrors.value.email = 'Formato de email incorrecto';
  }

  if (signupReq.password === '') {
    inputErrors.value.password = 'Campo obligatorio';
  } else if (!passRegex.test(signupReq.password)) {
    inputErrors.value.password = 'Mínimo 8 carácteres';
  }

  if (signupReq.password_confirmation === '') {
    inputErrors.value.password_confirmation = 'Campo obligatorio';
  } else if (signupReq.password_confirmation !== signupReq.password) {
    inputErrors.value.password_confirmation = 'Las contraseñas no coinciden';
  }
};



onMounted(() => {
  document.title = 'VC | Registro';
});
</script>


<template>
  <main>
    <img src="../assets/img/Logo Voz Ciudadana.svg" alt="" width="120" height="120">
    <h1>Registrarse</h1>
    <form @submit.prevent @submit="signup" novalidate>

      <!-- Usuario -->
      <div class="input-field col s6">
        <i class="material-icons prefix">face</i>
        <input type="text" name="username" id="username" class="validate" v-model="signupReq.username"
          :class="{ 'invalid': inputErrors.username }">
        <label for="username">Nombre de usuario</label>
        <span class="helper-text" :data-error="inputErrors.username" v-show="inputErrors.username"></span>
      </div>

      <!-- Email -->
      <div class="input-field col s6">
        <i class="material-icons prefix">mail</i>
        <input type="email" name="email" id="email" v-model="signupReq.email" class="validate"
          :class="{ 'invalid': inputErrors.email }">
        <label for="email">Correo electrónico</label>
        <span class="helper-text" :data-error="inputErrors.email" v-if="inputErrors.email"></span>
      </div>

      <!-- Pass -->
      <div class="input-field col s6">
        <i class="material-icons prefix">password</i>
        <input type="password" name="password" id="password" class="validate" v-model="signupReq.password"
          :class="{ 'invalid': inputErrors.password }">
        <label for="password">Contraseña</label>
        <span class="helper-text" :data-error="inputErrors.password" v-show="inputErrors.password"></span>
      </div>

      <!-- Confirm Pass -->
      <div class="input-field col s6">
        <i class="material-icons prefix">vpn_key</i>
        <input type="password" name="confirm_password" id="confirm_password" class="validate"
          v-model="signupReq.password_confirmation" :class="{ 'invalid': inputErrors.password_confirmation }">
        <label for="confirm_password">Confirmar contraseña</label>
        <span class="helper-text" :data-error="inputErrors.password_confirmation"
          v-show="inputErrors.password_confirmation"></span>
      </div>

      <!-- Sumbit -->
      <input type="submit" value="Registrarme">
      <div class="progress" v-show="isLoading">
        <div class="indeterminate"></div>
      </div>
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