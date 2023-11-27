<script setup>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
</script>

<template>
    <Header />
    <main class="quienes-somos-view">
        <h1>Visión</h1>
        <p>Ser la plataforma líder para la participación ciudadana en la mejora de la vía pública en México.</p>

        <h1>Misión</h1>
        <p>Facilitar a los ciudadanos mexicanos la reportación de incidentes o problemas en la vía pública, y promover la
            participación comunitaria y la revisión administrativa para verificar la validez y resolución de dichos
            reportes.</p>

        <p> La visión es inspiradora y ambiciosa, pero también es realista y alcanzable. Describe un futuro en el que la
            empresa es la principal plataforma para que los ciudadanos mexicanos participen en la mejora de la vía pública.

            La misión es clara y concisa, y es fácil de entender para todos los empleados de la empresa. Describe lo que la
            empresa hace y para quién lo hace.

            En particular, la visión y misión de esta empresa se destacan por los siguientes puntos:

            Se centran en los ciudadanos mexicanos: La empresa se compromete a servir a los ciudadanos mexicanos y a mejorar
            su calidad de vida.
            Enfatizan la participación ciudadana: La empresa cree que la participación ciudadana es esencial para la mejora
            de la vía pública.
            Reconocen la importancia de la revisión administrativa: La empresa comprende que la revisión administrativa es
            necesaria para garantizar la validez y resolución de los reportes. </p>

        <h1>Valores</h1>

        <p>Participación: La empresa cree en la importancia de la participación ciudadana para la mejora de la vía pública.
            Innovación: La empresa busca constantemente nuevas formas de mejorar su plataforma y sus servicios.
        </p>
        <p>Transparencia: La empresa se compromete a ser transparente con sus usuarios y con la comunidad.
            Responsabilidad: La empresa se compromete a ser responsable de sus acciones y a contribuir al bienestar de la
            sociedad.</p>
    </main>
    <Footer />
</template>

<style lang="scss" scoped>
main {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    min-height: 100vh;
    width: 90%;
    margin: 20px auto;
}

@media (width < 350px) {
    h1 {
        font-size: 2rem;
    }
}
</style>