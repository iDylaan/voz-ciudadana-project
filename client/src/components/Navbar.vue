<script setup>
import { ref, onMounted } from 'vue';
const menuActive = ref(false);

onMounted(() => {
    M.AutoInit();
});


const toggleMenu = () => {
    menuActive.value = !menuActive.value;
};
</script>


<template>
    <div class="vc-navbar">
        <ul id="slide-out" class="sidenav">
            <li>
                <div class="user-view">
                    <div class="background">
                        <img src="images/office.jpg">
                    </div>
                    <a href="#user"><img class="circle" src="images/yuna.jpg"></a>
                    <a href="#name"><span class="white-text name">John Doe</span></a>
                    <a href="#email"><span class="white-text email">jdandturk@gmail.com</span></a>
                </div>
            </li>
            <li><a href="#!"><i class="material-icons">cloud</i>First Link With Icon</a></li>
            <li><a href="#!">Second Link</a></li>
            <li>
                <div class="divider"></div>
            </li>
            <li><a class="subheader">Subheader</a></li>
            <li><a class="waves-effect" href="#!">Third Link With Waves</a></li>
        </ul>
        <div class="background__button">
            <button class="menu__icon sidenav-trigger" @click="toggleMenu" :class="menuActive ? 'menu__active' : ''"
                href="#" data-target="slide-out">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </div>
</template>


<style lang="scss" scoped>
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

.sidenav-overlay {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 998;
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
}</style>