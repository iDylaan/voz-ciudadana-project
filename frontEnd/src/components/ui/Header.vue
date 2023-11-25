<script setup>
import logo from '@/img/logo.svg'
const imgLogo = logo
</script>


<template>
    <header>
        <div class="header__container">
            <div class="logo__container">
                <img :src="imgLogo.src" alt="Logo Voz Ciudadana">
            </div>

            <div class="options__container">
                <p>Navbar</p>
            </div>
        </div>
    </header>
</template>

<style lang="css" scoped>
header {
    width: 100vw;
    position: fixed;
    top: 0;
    left: 0;
    display: grid;
    height: 60px;
    place-content: center;
    background-color: #082933;
    z-index: 1000;
}
.header__container {
    width: 98vw;
    margin: auto;
    display: flex;
    justify-content: space-between;
    
}

img {
    padding: 2px;
    border-radius: 10px;
    width: 100%;
    height: 100%;
}

.logo__container {
    width: 55px;
    height: 55px;
}
</style>