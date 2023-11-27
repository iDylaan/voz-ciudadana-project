<script setup>
import { ref, watch, defineProps, defineEmits, reactive, onMounted } from "vue";
import Swal from 'sweetalert2';
import { useStore } from "vuex";

const props = defineProps({
    "show": {
        type: Boolean,
        required: false,
        default: false
    }
});
const emit = defineEmits(['update:show']);
const showEditor = ref(props.show);
const profilePics = reactive({});
const store = useStore();
const step = ref(0);
const userData = reactive({});
const isLoading = ref(false);

watch(() => props.show, (newValue) => {
    showEditor.value = newValue;
});

onMounted(() => {
    profilePics.pic = '';
    profilePics.banner = '';
    step.value = 1;

    userData.username = store.state.auth.user.username;
    userData.email = store.state.auth.user.email;

    showEditor.value = JSON.parse(localStorage.getItem('first_access'));
});

const handlePic = (pic) => profilePics.pic = pic;
const setPicStep = () => step.value = 1;
const setBannerStep = () => step.value = 2;
const handleBanner = (banner) => profilePics.banner = banner;

const closeEditor = () => {
    showEditor.value = false;
    emit('update:show', false);
};

const updateProfileValues = async () => {
    isLoading.value = true;
    profilePics.user_id = store.state.auth.user.id;
    profilePics.token = localStorage.getItem('token');
    try {
        await store.dispatch('auth/updateProfileTheme', profilePics);
        Swal.fire({
            icon: 'success',
            title: 'Perfil actualizado!',
            text: 'Tu perfil ahora se ve más fresco!! ✨🤙'
        }).then((result) => {
            if (result.value) {
                store.commit('auth/setThemePorfile', profilePics);
                showEditor.value = false;
                emit('update:show', false);
            }
        });
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: error,
        })
    } finally {
        isLoading.value = false;
    }
};
</script>

<template>
    <div v-if="showEditor" class="profile-theme-editor">
        <span class="bg-toggler"></span>

        <div class="container">
            <div class="window-option__container" id="main-top">
                <button class="close-button" @click="closeEditor">
                    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink"
                        width="512" height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512"
                        xml:space="preserve" class="">
                        <g>
                            <path
                                d="M10.957 12.354a.5.5 0 0 1 0-.708l4.586-4.585a1.5 1.5 0 0 0-2.121-2.122L8.836 9.525a3.505 3.505 0 0 0 0 4.95l4.586 4.586a1.5 1.5 0 0 0 2.121-2.122Z"
                                opacity="1"></path>
                        </g>
                    </svg>
                    Salir
                </button>
            </div>
            <h5 style="padding-left: 10px;">Vamos a personalizar tu perfil!</h5>

            <!-- Picture Profile -->
            <div class="pic-profile-tab" v-show="step === 1">
                <label for="pic-profile">Escoge tu imágen de perfil</label>
                <div class="pics-profile">
                    <div class="pic" v-for="index in 20" :key="index" :class="{ 'pic-selected': profilePics.pic === index }"
                        @click="handlePic(index)">
                        <img :src="require(`@/assets/icon/profile-pictures/profilePic${index}.svg`)"
                            :alt="`Imagen de perfil`">
                    </div>
                </div>
                <div class="pics-buttons" id="#pic-next">
                    <a class="waves-effect waves-light btn" style="background-color: var(--BgQuaternary);" :class="{ 'disabled': profilePics.pic <= 0 }"
                        @click="setBannerStep" href="#main-top">Continuar</a>
                </div>
            </div>

            <!-- Banner Profile -->
            <div class="banner-profile-tab" v-show="step === 2" id="banner-profile__container">

                <div class="user-view">
                    <div class="background"
                        :style="{ backgroundImage: `url(${require('@/assets/img/profile-banners/banner' + (profilePics.banner > 0 ? profilePics.banner : 1) + '.svg')}` }">
                        <span class="black-opacity"></span>
                    </div>
                    <a href="#"><img class="circle"
                            :src="require(`@/assets/icon/profile-pictures/profilePic${profilePics.pic > 0 ? profilePics.pic : 1}.svg`)"></a>
                    <a href="#"><span class="white-text name">{{ userData.username }}</span></a>
                    <a href="#"><span class="white-text email">{{ userData.email }}</span></a>
                </div>

                <label for="pic-profile">Escoge tu banner de perfil</label>
                <div class="banners-profile">
                    <div class="banner" v-for="index in  14 " :key="index"
                        :class="{ 'banner-selected': profilePics.banner === index }" @click="handleBanner(index)"
                        :style="{ backgroundImage: `url(${require('@/assets/img/profile-banners/banner' + index + '.svg')}` }">
                    </div>
                </div>
                <div class="pics-buttons" id="#pic-next">
                    <a class="waves-effect waves-light btn-flat grey darken-1" style="color: white;"
                        @click="setPicStep">Regresar</a>
                    <a class="waves-effect waves-light btn" style="background-color: var(--BgQuaternary);" @click="updateProfileValues"
                        :class="{ 'disabled': profilePics.banner <= 0 }">Terminar</a>
                </div>
                <div class="progress" v-show="isLoading">
                    <div class="indeterminate"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@keyframes parallaxFadeIn {
    0% {
        transform: translateY(-50px);
        opacity: 0;
    }

    100% {
        transform: translateY(0);
        opacity: 1;
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.profile-theme-editor {
    position: absolute;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: 1001;
    display: grid;
    place-content: center;

    .pics-buttons {
        width: 100%;
        display: flex;
        justify-content: flex-end;
        padding: 10px 0;
        gap: 10px;
    }

    .bg-toggler {
        position: absolute;
        width: 100%;
        height: 100%;
        z-index: 1001;
        top: 0;
        left: 0;
        background-color: rgba(0, 0, 0, 0.591);
        -webkit-backdrop-filter: blur(12px);
        backdrop-filter: blur(12px);
        opacity: 0;
        animation: fadeIn 0.75s forwards;

        @supports not ((-webkit-backdrop-filter: blur(12px)) or (backdrop-filter: blur(12px))) {
            background-color: rgba(0, 0, 0, 0.8);
        }
    }

    .container {
        position: relative;
        width: calc(100vw - 10px);
        height: calc(100vh - 100px);
        background-color: white;
        overflow-y: auto;
        z-index: 1002;
        border-radius: 5px;
        animation: parallaxFadeIn 0.75s forwards;

        .banner-profile-tab {
            width: 100%;
            padding: 10px;
            position: sticky;

            .go-to-top-floating-button {
                position: fixed;
                left: 10px;
                bottom: 25px;
            }

            .banners-profile {
                padding: 10px 0;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                grid-gap: 5px;
                place-items: center;

                .user-view {
                    border: 1px solid red;
                }

                .banner {
                    box-shadow: 0 0 0 2px rgb(216, 216, 216);
                    cursor: pointer;
                    transition: all 0.1s ease-in-out;
                    width: 300px;
                    height: 150px;
                    background-repeat: repeat;



                    &:hover {
                        box-shadow: 0 0 0 2px rgb(128, 128, 128);
                    }

                    &.banner-selected {
                        box-shadow: 0 0 0 3px var(--BgTertiary);

                        &:hover {
                            box-shadow: 0 0 0 3px var(--BgTertiary);
                        }
                    }

                }
            }
        }

        .pic-profile-tab {
            width: 100%;
            padding: 10px;

            .pics-profile {
                padding: 10px 0px;
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                grid-gap: 5px;


                .pic {
                    padding: 5px;
                    box-shadow: 0 0 0 2px rgb(216, 216, 216);
                    border-radius: 1000px;
                    cursor: pointer;
                    transition: all 0.1s ease-in-out;

                    &:hover {
                        box-shadow: 0 0 0 2px rgb(128, 128, 128);

                        img {
                            transition: transform 0.3s ease;
                            transform: scale(1.05);
                        }
                    }

                    &.pic-selected {
                        box-shadow: 0 0 0 3px var(--BgTertiary);
                        background-color: var(--BgHigher1);

                        img {
                            transition: transform 0.3s ease;
                            transform: scale(1.05);
                        }

                        &:hover {
                            box-shadow: 0 0 0 3px var(--BgTertiary);
                        }

                    }

                    img {
                        width: 100%;
                        height: 100%;
                    }
                }
            }
        }

        .window-option__container {
            width: 100%;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            padding: 5px;

            .close-button {
                border: none;
                outline: none;
                background-color: transparent;
                border-radius: 5px;
                padding: 5px;
                display: flex;
                align-items: center;
                justify-content: flex-start;
                gap: 10px;
                position: relative;
                font-size: 1.1rem;

                svg {
                    color: #262626;
                    fill: #262626;
                    width: 18px;
                    height: 18px;
                }

                &:hover {

                    &::before {
                        content: '';
                        position: absolute;
                        bottom: 0;
                        right: 0;
                        width: 60px;
                        height: 2px;
                        background-color: rgba(0, 0, 0, 0.5);
                        border-radius: 5px;
                    }
                }
            }
        }
    }
}

.user-view {
    width: 100%;
    margin: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-top: 60px;
    /* Ajustar según sea necesario para el espacio por encima de la imagen */
    padding-bottom: 20px;
    /* Ajustar según sea necesario para el espacio debajo del texto */
    position: relative;
    width: 300px;
    /* Ancho del banner */
    height: 150px;
    /* Altura total de la tarjeta, ajustar según sea necesario */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    /* Sombra de la tarjeta */
}

.background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 150px;
    /* Altura del banner */
    background-size: cover;
    /* Asegurar que el fondo cubra completamente el área */
    background-position: center;
    /* Centrar el fondo */
    z-index: -1;
}

.black-opacity {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 150px;
    /* Altura del banner */
    background-color: rgba(0, 0, 0, 0.3);
    /* Opacidad sobre el banner */
    z-index: 0;
}

.circle {
    border-radius: 50%;
    width: 80px;
    height: 80px;
    border: 4px solid white;
    /* Ajusta el borde según tu diseño */
    margin-top: -40px;
    /* La mitad del tamaño del círculo */
    z-index: 1;
    background-color: white;
    /* Fondo blanco para la imagen del perfil */
}

.name,
.email {
    color: white;
    text-align: center;
    /* Centrar el texto */
    z-index: 1;
}


@media (width < 700px) {}

@media (width < 700px) {
    .profile-theme-editor {
        .container {
            .pic-profile-tab {
                .pics-profile {
                    grid-template-columns: repeat(4, 1fr);
                }
            }
        }
    }
}

@media (width < 500px) {
    .profile-theme-editor {
        .container {
            .pic-profile-tab {
                .pics-profile {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
        }
    }
}
</style>