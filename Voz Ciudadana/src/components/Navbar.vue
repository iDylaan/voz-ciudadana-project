<script setup>
import { useStore } from 'vuex';
import { useRouter, onBeforeRouteLeave } from 'vue-router';
import { ref, onMounted, onBeforeUnmount, computed, reactive, watch } from 'vue';
import { tokenExpired } from "@/utils/misc.js";
import ProfileThemeEditor from "@/components/ProfileThemeEditor.vue";

const router = useRouter();
const store = useStore();
const menuActive = ref(false);
const token = ref(localStorage.getItem("token") ? localStorage.getItem("token") : '');
const authed = ref(false);
const isEditorVisible = ref(false);

const userData = reactive(store.state.auth.user);

const openProfileEditor = () => isEditorVisible.value = true;
const closeProfileEditor = () => isEditorVisible.value = false;

const closeSidenav = () => {
    const instance = M.Sidenav.getInstance(document.querySelector('.sidenav'));
    if (instance && instance.isOpen) {
        instance.close();
        menuActive.value = false;
    }
};

const userImageSrc = computed(() => {
    return userData.profile_picture ? require(`@/assets/icon/profile-pictures/profilePic${userData.profile_picture}.svg`) : '';
});

const userBannerStyle = computed(() => {
    return userData.profile_banner ? `url(${require(`@/assets/img/profile-banners/banner${userData.profile_banner}.svg`)})` : '';
});

// Watcher para reaccionar a los cambios de ruta
watch(() => router.currentRoute.value, () => {
    closeSidenav();
});

watch(() => store.state.auth.user, (user) => {
    userData.profile_picture = user.profile_picture;
    userData.profile_banner = user.profile_banner;
})

// Asegúrate de que se cierre el sidenav cuando la ruta cambia.
onBeforeRouteLeave(() => {
    closeSidenav();
});

onMounted(() => {
    authed.value = !tokenExpired(token.value);
    M.AutoInit();

    // Inicializar el sidenav de Materialize
    M.Sidenav.init(document.querySelector('.sidenav'), {
        onCloseEnd: () => {
            menuActive.value = false;
        },
    });
});

onBeforeUnmount(() => {
    // Destruye la instancia de Sidenav para limpiar event listeners que agrega Materialize internamente.
    const instance = M.Sidenav.getInstance(document.querySelector('.sidenav'));
    if (instance) {
        instance.destroy();
    }
});

const toggleMenu = () => {
    menuActive.value = !menuActive.value;

    if (menuActive.value) {
        M.Sidenav.getInstance(document.querySelector('.sidenav')).open();
    } else {
        closeSidenav();
    }
};

const logout = () => {
    store.dispatch('auth/logout');
    authed.value = false;
    router.push('/login');
};
</script>

<template>
    <div class="vc-navbar">
        <ProfileThemeEditor :show="isEditorVisible" @update:show="isEditorVisible = $event" />

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

            <li><router-link @click="closeSidenav" class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">home</i>Inicio</router-link></li>
            <li><router-link @click="closeSidenav" class="waves-effect sidenav-close" to="/reports"><i
                        class="material-icons">reports</i>Reportes</router-link></li>
            <li><router-link @click="closeSidenav" class="waves-effect sidenav-close" to="/map-reports"><i
                        class="material-icons">map</i>Mapa de
                    reportes</router-link></li>
            <li v-if="authed"><router-link @click="closeSidenav" class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">dashboard</i>Dashboard</router-link></li>
            <li v-if="authed">
                <div class="divider"></div>
            </li>
            <li v-if="authed"><router-link @click="closeSidenav" class="waves-effect sidenav-close" to="/new-report"><i
                        class="material-icons">format_list_bulleted_add</i>Nuevo
                    reporte</router-link></li>
            <li v-if="authed"><router-link @click="closeSidenav" class="waves-effect sidenav-close" to="/"><i
                        class="material-icons">list_alt</i>Mis
                    reportes</router-link></li>
            <li>
                <div class="divider"></div>
            </li>
            <li v-if="!authed"><router-link @click="closeSidenav" class="waves-effect sidenav-close" to="/login"><i
                        class="material-icons">login</i>Iniciar
                    Sesión</router-link></li>
            <li v-if="authed"><a class="waves-effect sidenav-close" @click="openProfileEditor"><i
                        class="material-icons">manage_accounts</i>Editar Perfil</a></li>
            <li v-if="authed"><a class="waves-effect sidenav-close" @click="logout"><i
                        class="material-icons">logout</i>Cerrar Sesión</a></li>
            <li><router-link class="waves-effect sidenav-close" to="/quienes-somos"><i
                        class="material-icons">groups</i>Quienes Somos</router-link></li>
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