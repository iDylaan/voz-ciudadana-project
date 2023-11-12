<script setup>
import { ref, onMounted, reactive } from "vue";

const props = defineProps({
    firstAccess: {
        type: Boolean,
        required: false,
        default: false,
    }
});

const showEditor = ref(true);
const profilePics = reactive({});


onMounted(async () => {
    profilePics.pic = '';
    profilePics.banner = '';
});

</script>

<template>
    <div v-if="showEditor" class="profile-theme-editor">
        <span class="bg-toggler"></span>

        <div class="container">
            <div class="window-option__container">
                <button class="close-button">
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

            <div class="pic-profile-tab">
                <label for="pic-profile">Escoge tu imágen de perfil</label>
                <div class="pics-profile">
                    <div class="pic" v-for="index in 20" :key="index">
                        <img :src="require(`@/assets/icon/profile-pictures/profilePic${index}.svg`)"
                            :alt="`Imagen de perfil`">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.profile-theme-editor {
    position: absolute;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: 1001;
    display: grid;
    place-content: center;

    .container {
        position: relative;
        width: calc(100vw - 10px);
        height: calc(100vh - 100px);
        background-color: white;
        overflow-y: auto;
        z-index: 1002;
        border-radius: 5px;

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
                    border: 1px solid rgb(216, 216, 216);
                    border-radius: 100px;
                    cursor: pointer;

                    &:hover {
                        border: 1px solid rgb(128, 128, 128);

                        img {
                            transition: transform 0.3s ease;
                            transform: scale(1.05);
                        }
                    }

                    &.pic-selected {
                        border: 1px solid #0f445b;
                        background-color: #1f6d88;

                        img {
                            transition: transform 0.3s ease;
                            transform: scale(1.05);
                        }

                        &:hover {
                            border: 1px solid #0f445b;
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


    .bg-toggler {
        position: absolute;
        width: 100%;
        height: 100%;
        z-index: 1001;
        top: 0;
        left: 0;
        background-color: rgba(0, 0, 0, 0.324);
        backdrop-filter: blur(12px);
    }
}


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