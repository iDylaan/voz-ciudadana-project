<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { ref, onMounted, onBeforeUnmount, computed, reactive } from 'vue';
import { tokenExpired } from "@/utils/misc.js";

const router = useRouter();
const store = useStore();
const menuActive = ref(false);
const token = ref(localStorage.getItem("token") ? localStorage.getItem("token") : '');
const authed = ref(false);

const userData = reactive({
    username: null,
    email: null,
    isAdmin: null,
    picProfile: null,
    bannerProfile: null,
});

const userImageSrc = computed(() => {
    return userData.picProfile !== null ? require(`@/assets/icon/profile-pictures/profilePic${userData.picProfile}.svg`) : '';
});

const userBannerStyle = computed(() => {
    return userData.bannerProfile !== null ? `url(${require(`@/assets/img/profile-banners/banner${userData.bannerProfile}.svg`)})` : '';
});

onMounted(() => {
    authed.value = !tokenExpired(token.value);
    console.log(authed.value);
    M.AutoInit();

    // Reset menuActive
    M.Sidenav.getInstance(document.querySelector('.sidenav')).close();

    // Añade el listener después de que el componente y Materialize estén inicializados
    document.addEventListener('click', (e) => {
        // Comprueba si el clic fue en el sidenav-overlay
        if (e.target.classList.contains('sidenav-overlay')) {
            handleOverlayClick();
        } else if (e.target.classList.contains('sidenav-close')) {
            toggleMenu();
        }
    });


    userData.username = store.state.auth.user.username || localStorage.getItem('username');
    userData.email = store.state.auth.user.email || localStorage.getItem('email');
    userData.isAdmin = store.state.auth.user.isAdmin || localStorage.getItem('is_admin');
    userData.picProfile = store.state.auth.user.picProfile || localStorage.getItem('pic_profile');
    userData.bannerProfile = store.state.auth.user.bannerProfile || localStorage.getItem('banner_profile');
});

onBeforeUnmount(() => {
    // Elimina el listener para prevenir fugas de memoria
    document.removeEventListener('click', (e) => {
        if (e.target.classList.contains('sidenav-overlay')) {
            handleOverlayClick();
        } else if (e.target.classList.contains('sidenav-close')) {
            toggleMenu();
        }
    });
});


const toggleMenu = () => {
    menuActive.value = !menuActive.value;

    if (menuActive.value) {
        M.Sidenav.getInstance(document.querySelector('.sidenav')).open();
    } else {
        M.Sidenav.getInstance(document.querySelector('.sidenav')).close();
    }
};

const handleOverlayClick = () => {
    menuActive.value = false;
};

const logout = () => {
    store.dispatch('auth/logout');
    authed.value = false;
};
</script>




<template>
    <div class="vc-navbar">
        <ul id="slide-out" class="sidenav">
            <li v-if="authed">
                <div class="user-view">
                    <div class="background" :style="{ backgroundImage: userBannerStyle }">
                        <span class="black-opacity"></span>
                    </div>
                    <a href="#user-pic"><img class="circle" :src="userImageSrc"></a>
                    <a href="#namename"><span class="white-text name">{{ userData.username }}</span></a>
                    <a href="#email"><span class="white-text email">{{ userData.email }}</span></a>
                </div>
            </li>

            <li><router-link class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">home</i>Inicio</router-link></li>
            <li><router-link class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">reports</i>Reportes</router-link></li>
            <li><router-link class="waves-effect sidenav-close" to="/"><i class="material-icons">map</i>Mapa de
                    reportes</router-link></li>
            <li v-if="authed"><router-link class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">dashboard</i>Dashboard</router-link></li>
            <li v-if="authed">
                <div class="divider"></div>
            </li>
            <li v-if="authed"><router-link class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">format_list_bulleted_add</i>Nuevo
                    reporte</router-link></li>
            <li v-if="authed"><router-link class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">list_alt</i>Mis
                    reportes</router-link></li>
            <li>
                <div class="divider"></div>
            </li>
            <li v-if="!authed"><router-link class="waves-effect sidenav-close" to="/login"><i
                        class="material-icons">login</i>Iniciar
                    Sesión</router-link></li>
            <li v-if="authed"><a class="waves-effect sidenav-close" @click="logout"><i
                        class="material-icons">logout</i>Cerrar Sesión</a></li>
        </ul>
        <div class="background__button">
            <button class="menu__icon" @click="toggleMenu" :class="menuActive ? 'menu__active' : ''"
                data-target="slide-out">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </div>
</template>


<style lang="scss" scoped>
@media only screen and (min-width: 992px) {
    .user-view {
        padding: 16px 16px 0;
    }
}


.vc-navbar {
    position: static;
}

.circle {
    background-color: white;
    padding: 3px;
    box-shadow:
        0px 0.9px 2.2px rgba(0, 0, 0, 0.011),
        0px 2.1px 5.3px rgba(0, 0, 0, 0.016),
        0px 3.9px 10px rgba(0, 0, 0, 0.02),
        0px 6.9px 17.9px rgba(0, 0, 0, 0.024),
        0px 13px 33.4px rgba(0, 0, 0, 0.029),
        0px 31px 80px rgba(0, 0, 0, 0.04);
}

.background {
    background-repeat: repeat;
    position: relative;
    height: 150px;

    .black-opacity {
        position: absolute;
        /* Esto saca al elemento del flujo normal y lo posiciona en relación a su contenedor más cercano con posición relativa o absoluta */
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.2);
        /* Color negro con opacidad, no es necesario el `opacity` si usas rgba */
        width: 100%;
        height: 100%;
    }
}

/* <reset-style> ============================ */
button {
    border: none;
    background: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
    font-family: inherit;
}

/* ============================ */
/* <style for bg> ======== */
.background__button {
    mix-blend-mode: luminosity;
    backdrop-filter: blur(15px);
    width: 55px;
    height: 55px;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* <style for menu__icon> ======== */
.menu__icon {
    width: 32px;
    height: 32px;
    padding: 4px;
}

.menu__icon span {
    display: block;
    width: 100%;
    height: 0.125rem;
    border-radius: 2px;
    background-color: rgb(255, 255, 255);
    transition: background-color .4s;
    position: relative;
}

.menu__icon span+span {
    margin-top: .375rem;
}

.menu__icon span:nth-child(1) {
    animation: ease .8s menu-icon-top-2 forwards;
}

.menu__icon span:nth-child(2) {
    animation: ease .8s menu-icon-scaled-2 forwards;
}

.menu__icon span:nth-child(3) {
    animation: ease .8s menu-icon-bottom-2 forwards;
}

.menu__active span:nth-child(1) {
    animation: ease .8s menu-icon-top forwards;
}

.menu__active span:nth-child(2) {
    animation: ease .8s menu-icon-scaled forwards;
}

.menu__active span:nth-child(3) {
    animation: ease .8s menu-icon-bottom forwards;
    background-color: rgb(255, 59, 48);
}

@keyframes menu-icon-top {
    0% {
        top: 0;
        transform: rotate(0);
    }

    50% {
        top: .5rem;
        transform: rotate(0);
    }

    100% {
        top: .5rem;
        transform: rotate(45deg);
    }
}

@keyframes menu-icon-top-2 {
    0% {
        top: .5rem;
        transform: rotate(45deg);
    }

    50% {
        top: .5rem;
        transform: rotate(0);
    }

    100% {
        top: 0;
        transform: rotate(0);
    }
}

@keyframes menu-icon-bottom {
    0% {
        bottom: 0;
        transform: rotate(0);
    }

    50% {
        bottom: .5rem;
        transform: rotate(0);
    }

    100% {
        bottom: .5rem;
        transform: rotate(135deg);
    }
}

@keyframes menu-icon-bottom-2 {
    0% {
        bottom: .5rem;
        transform: rotate(135deg);
    }

    50% {
        bottom: .5rem;
        transform: rotate(0);
    }

    100% {
        bottom: 0;
        transform: rotate(0);
    }
}

@keyframes menu-icon-scaled {
    50% {
        transform: scale(0);
    }

    100% {
        transform: scale(0);
    }
}

@keyframes menu-icon-scaled-2 {
    0% {
        transform: scale(0);
    }

    50% {
        transform: scale(0);
    }

    100% {
        transform: scale(1);
    }
}
</style>