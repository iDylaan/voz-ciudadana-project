<script setup>
import { ref, onMounted } from 'vue';
const daltonismState = ref(localStorage.getItem('daltonism') || '')
const daltonismTypes = [
    'protanopia',
    'deuteranopia',
    'tritanopia',
    'acromatopsia',
    'protanomalia',
    'deuteranomalia',
    'tritanomalia',
    'acromatomalia',
]

onMounted(() => {
    if (daltonismState.value) document.documentElement.classList.add(daltonismState.value);
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
})

const handleDaltonism = (type) => {
    localStorage.setItem('daltonism', String(type));
    daltonismTypes.forEach((type) => {
        document.documentElement.classList.remove(type);
    });
    document.documentElement.classList.add(type);
};
</script>

<template>
    <div class="input-field">
        <div class="select">
            <select class="input-daltonism" @change="handleDaltonism($event.target.value)">
                <option value="" disabled :selected="daltonismState === ''">Filtro para daltonismo</option>
                <option value="none">Ninguno</option>
                <option :selected="daltonismState === 'protanopia'" value="protanopia">Protanopia</option>
                <option :selected="daltonismState === 'deuteranopia'" value="deuteranopia">Deuteranopia</option>
                <option :selected="daltonismState === 'tritanopia'" value="tritanopia">Tritanopia</option>
                <option :selected="daltonismState === 'acromatopsia'" value="acromatopsia">Acromatopsia</option>
                <option :selected="daltonismState === 'protanomalia'" value="protanomalia">Protanomalía</option>
                <option :selected="daltonismState === 'deuteranomalia'" value="deuteranomalia">Deuteranomalía</option>
                <option :selected="daltonismState === 'tritanomalia'" value="tritanomalia">Tritanomalía</option>
                <option :selected="daltonismState === 'acromatomalia'" value="acromatomalia">Acromatomalía</option>
            </select>
            <label style="font-size: 1rem;"><i class="material-icons" style="font-size: 1rem;">palette</i> Filtro para daltonismo</label>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.input-daltonismo {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
}
</style>