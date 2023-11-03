<script setup>
import Navbar from '@/components/Navbar.vue';
</script>


<template>
    <header>
        <div class="header__container">
            <div class="logo__container">
                <img src="@/assets/img/Logo Voz Ciudadana Fondos Oscuros.svg" alt="Logo Voz Ciudadana">
            </div>

            <div class="options__container">
                <Navbar />
            </div>
        </div>
    </header>
</template>

<style lang="scss" scoped>
header {
    width: 100vw;
    position: fixed;
    top: 0;
    left: 0;
    display: grid;
    height: 60px;
    place-content: center;
    background-color: #082933;
    
    .header__container {
        width: 98vw;
        margin: auto;
        display: flex;
        justify-content: space-between;

        .logo__container {
            width: 55px;
            height: 55px;
            img {
                padding: 2px;
                border-radius: 10px;
                width: 100%;
                height: 100%;
            }
        }


        .options__container {

        }

    }
}
</style>