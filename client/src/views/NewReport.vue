<script setup>
import Header from "@/components/Header.vue";
</script>

<template>
    <Header />
    <main class="container">
        <h1 class="center-align">Nuevo Reporte ⚠️</h1>

        <div class="row">
            <form @submit.prevent="submitReport" class="col s12">
                <div class="input-field col s12">
                    <input id="report_title" type="text" v-model="reportTitle" required>
                    <label for="report_title">Título del Reporte</label>
                </div>
                <div class="input-field col s12">
                    <textarea id="report_description" class="materialize-textarea" v-model="reportDescription"
                        required></textarea>
                    <label for="report_description">Descripción</label>
                </div>
                <div class="input-field col s12">
                    <select id="report_category" v-model="reportCategory" required>
                        <option value="" disabled selected>Elige una categoría</option>
                        <option value="categoria1">Categoría 1</option>
                        <option value="categoria2">Categoría 2</option>
                        <!-- Añade más categorías según sea necesario -->
                    </select>
                    <label for="report_category">Categoría</label>
                </div>
                <div class="file-field input-field col s12">
                    <div class="btn">
                        <span>Archivo</span>
                        <input type="file" @change="reportImage = $event.target.files[0]" accept="image/*">
                    </div>
                    <div class="file-path-wrapper">
                        <input class="file-path validate" type="text" placeholder="Subir una imagen del reporte">
                    </div>
                </div>
                <div class="col s12">
                    <button type="submit" class="btn waves-effect waves-light">Enviar Reporte</button>
                </div>
            </form>
        </div>
    </main>
</template>


<style lang="scss" scoped>
main {
    min-height: 100vh;
    padding: 2rem 0;
    background-color: #fcfcfc;
    width: 100%;

    .form {
        margin-top: 2rem;
        form {
            padding: 0 2rem;

            .input-field {
                margin-bottom: 1.5rem;
            }

            button {
                width: 100%;
                margin-top: 1rem;
            }
        }
    }
}
</style>
