<template>
    <footer class="pie-pagina">
        <div class="grupo-1">
            <div class="box">
                <figure>
                    <a href="#">
                        <img class="logo" src="@/assets/img/Logo Voz Ciudadana Fondos Oscuros.svg" alt="Logo de LIFO">
                    </a>
                </figure>
            </div>
            <div class="box">
                <h2>SOBRE NOSOTROS</h2>
                <p>En Voz Ciudadana, nos dedicamos a fortalecer el tejido social y empoderar a los ciudadanos para construir
                    comunidades más seguras y colaborativas. Nuestra plataforma digital ofrece una vía efectiva para que los
                    ciudadanos reporten incidentes en la vía pública y participen activamente en la mejora de su entorno.
                </p>
            </div>
            <div class="box">
                <h2>Contactanos</h2>
                <p>lifoUnt@gmail.com</p>
                <p>55-23-25-85-96</p>
            </div>
            <div class="box">
                <h2>SIGUENOS</h2>
                <div class="red-social">
                    <a href="#" class="fa fa-facebook"></a>
                    <a href="#" class="fa fa-instagram"></a>
                    <a href="#" class="fa fa-twitter"></a>
                    <a href="#" class="fa fa-youtube"></a>
                </div>
            </div>
        </div>
        <div class="grupo-2">
            <small>&copy; 2023 <b>LIFO.</b> Todos los Derechos Reservados.</small>
        </div>
    </footer>
</template>


<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Open Sans', sans-serif;
}

.pie-pagina {
    width: 100%;
    background-color: #0a141d;
}

.pie-pagina .grupo-1 {
    width: 100%;
    max-width: 1200px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 50px;
    padding: 45px 0px;
}

.pie-pagina .grupo-1 .box figure {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.pie-pagina .grupo-1 .box figure img {
    width: 250px;
}

.pie-pagina .grupo-1 .box h2 {
    color: #fff;
    margin-bottom: 25px;
    font-size: 20px;
}

.pie-pagina .grupo-1 .box p {
    color: #efefef;
    margin-bottom: 10px;
}

.pie-pagina .grupo-1 .red-social a {
    display: inline-block;
    text-decoration: none;
    width: 45px;
    height: 45px;
    line-height: 45px;
    color: #fff;
    margin-right: 10px;
    background-color: #0d2033;
    text-align: center;
    transition: all 300ms ease;
}

.pie-pagina .grupo-1 .red-social a:hover {
    color: aqua;
}

.pie-pagina .grupo-2 {
    background-color: #0a1a2a;
    padding: 15px 10px;
    text-align: center;
    color: #fff;
}

.pie-pagina .grupo-2 small {
    font-size: 15px;
}

@media screen and (max-width:800px) {
    .pie-pagina .grupo-1 {
        width: 90%;
        grid-template-columns: repeat(1, 1fr);
        grid-gap: 30px;
        padding: 35px 0px;
    }
}

.box {
    figure {
        margin: 0;

        a {
            .logo {
                width: 70px;
                height: 70px;
            }
        }
    }
}
</style>