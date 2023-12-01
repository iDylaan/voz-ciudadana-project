<script setup>
import { onMounted, reactive, computed } from 'vue';
import { useStore } from 'vuex';
import Swal from 'sweetalert2';
import { reportApi } from '@/api/reports_api';

const store = useStore();
const signupReq = reactive({
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
  },
  password_confirmation: {
    value: '',
    valid: false,
    error: null,
    touched: false
  },
  username: {
    value: '',
    valid: false,
    error: null,
    touched: false
  }
});

const isLoading = computed(() => store.state.auth.isFormLoading);
const validInputs = computed(() => (
  signupReq.email.valid &&
  signupReq.password.valid &&
  signupReq.password_confirmation.valid &&
  signupReq.username.valid
));

const signup = async () => {
  if (!validInputs.value) return;

  try {
    await store.dispatch('auth/signup', {
      email: signupReq.email.value,
      password: signupReq.password.value,
      password_confirmation: signupReq.password_confirmation.value,
      username: signupReq.username.value
    });
  } catch (error) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Hubo un error en el registro, inténtelo de nuevo más tarde.'
    });
  }
}

const userRegex = /^(?=.*[A-Za-z])[A-Za-z\d]{3,}$/;
const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

const validateUsername = () => {
  signupReq.username.touched = true;
  signupReq.username.valid = false;

  if (signupReq.username.value === '') {
    signupReq.username.error = 'El nombre de usuario es un campo obligatorio';
    return;
  }

  if (/\s/.test(signupReq.username.value)) {
    signupReq.username.error = 'El nombre de usuario no debe contener espacios';
    return;
  }

  if (!/^[A-Za-z]/.test(signupReq.username.value)) {
    signupReq.username.error = 'El nombre de usuario debe iniciar con una letra';
    return;
  }

  if (!userRegex.test(signupReq.username.value)) {
    signupReq.username.error = 'El nombre de usuario debe tener al menos 3 caracteres';
    return;
  }

  signupReq.username.valid = true;
  signupReq.username.error = null;
}


const validateEmail = async () => {
  signupReq.email.touched = true;
  signupReq.email.valid = false;

  if (signupReq.email.value === '') {
    signupReq.email.error = 'El correo electrónico es un campo obligatorio';
    return;
  }

  if (!emailRegex.test(signupReq.email.value)) {
    signupReq.email.error = 'Formato de email incorrecto';
    return;
  }

  try {
    const response = await reportApi.get('/get_email_exists/' + signupReq.email.value);
    const result = response.data;

    if (result.status === 'OK') {
      signupReq.email.error = 'Este correo electrónico no está disponible';
      return;
    } else {
      if (result.status === 'NOT_FOUND') {
        signupReq.email.valid = true;
        signupReq.email.error = null;
      } else {
        throw new Error();
      }
    }
  } catch (error) {
    signupReq.email.error = 'No se pudo validar la existencia del correo electrónico, intente de nuevo';
    return;
  }
}


const validatePassword = () => {
  signupReq.password.touched = true;
  signupReq.password.valid = true;
  signupReq.password.error = null;

  if (signupReq.password.value === '') {
    signupReq.password.valid = false;
    signupReq.password.error = 'La contraseña es un campo obligatorio';
    return;
  }

  const minEightChars = /.{8,}/;
  const hasUpperCase = /[A-Z]/;
  const hasLowerCase = /[a-z]/;
  const hasDigit = /\d/;

  if (!minEightChars.test(signupReq.password.value)) {
    signupReq.password.valid = false;
    signupReq.password.error = 'La contraseña debe tener al menos 8 caracteres';
  } else if (!hasUpperCase.test(signupReq.password.value)) {
    signupReq.password.valid = false;
    signupReq.password.error = 'La contraseña debe tener al menos una letra mayúscula';
  } else if (!hasLowerCase.test(signupReq.password.value)) {
    signupReq.password.valid = false;
    signupReq.password.error = 'La contraseña debe tener al menos una letra minúscula';
  } else if (!hasDigit.test(signupReq.password.value)) {
    signupReq.password.valid = false;
    signupReq.password.error = 'La contraseña debe tener al menos un dígito numérico';
  }
}


const validatePasswordConfirmation = () => {
  signupReq.password_confirmation.touched = true;
  signupReq.password_confirmation.valid = false;

  if (signupReq.password_confirmation.value === '') {
    signupReq.password_confirmation.error = 'La confirmación de la contraseña es un campo obligatorio';
    return;
  }

  if (signupReq.password_confirmation.value !== signupReq.password.value) {
    signupReq.password_confirmation.error = 'Las contraseñas no coinciden';
    return;
  }

  signupReq.password_confirmation.valid = true;
  signupReq.password_confirmation.error = null;
}


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
        <input type="text" name="username" id="username" v-model.trim="signupReq.username.value" @blur="validateUsername"
          :class="{ 'invalid': signupReq.username.touched ? !signupReq.username.valid : false }">
        <label for="username">Nombre de usuario</label>
        <span class="helper-text" :data-error="signupReq.username.error" v-show="signupReq.username.error"></span>
      </div>

      <!-- Email -->
      <div class="input-field col s6">
        <i class="material-icons prefix">mail</i>
        <input type="email" name="email" id="email" v-model.trim="signupReq.email.value" @blur="validateEmail"
          :class="{ 'invalid': signupReq.email.touched ? !signupReq.email.valid : false }">
        <label for="email">Correo electrónico</label>
        <span class="helper-text" :data-error="signupReq.email.error" v-show="signupReq.email.error"></span>
      </div>

      <!-- Pass -->
      <div class="input-field col s6">
        <i class="material-icons prefix">password</i>
        <input type="password" name="password" id="password" v-model.trim="signupReq.password.value"
          @blur="validatePassword" :class="{ 'invalid': signupReq.password.touched ? !signupReq.password.valid : false }">
        <label for="password">Contraseña</label>
        <span class="helper-text" :data-error="signupReq.password.error" v-show="signupReq.password.error"></span>
      </div>

      <!-- Confirm Pass -->
      <div class="input-field col s6">
        <i class="material-icons prefix">vpn_key</i>
        <input type="password" name="confirm_password" id="confirm_password" @input="validatePasswordConfirmation"
          v-model.trim="signupReq.password_confirmation.value"
          :class="{ 'invalid': signupReq.password_confirmation.touched ? !signupReq.password_confirmation.valid : false }">
        <label for="confirm_password">Confirmar contraseña</label>
        <span class="helper-text" :data-error="signupReq.password_confirmation.error"
          v-show="signupReq.password_confirmation.error"></span>
      </div>

      <!-- Sumbit -->
      <button type="submit" class="waves-effect waves-light btn-large"
        :class="{ 'disabled': !validInputs }">Registrarme</button>
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

.input-text-error {
  color: red;
  border-bottom: 1px solid black;
  box-shadow: 0 1px 0 0 red;
}

.btn-large {
  background-color: var(--BgSecondary);
  color: white;
}
</style>