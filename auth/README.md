# Guia para Auth API --tiutlo 1

esta api se desarrollo sobre el framework PHP Laravel que nos permite llevar a cabo la autenticacion de forma segura mediante API Tokens

## Pre-requisitos
1. **PHP versión**
    Puedes usar la version 8.1.1
2. **Composer**
    Puedes usar la version 2.6.5

    Puedes seguir el siguiente video para facilitar la instalacion de composer
    ```bash
    https://www.youtube.com/watch?v=pS0U-PsXUlg
    ```

## Configuracion de PHP

1. En la carpeta donde instalaste PHP, buscar el archivo "php.ini"
2. Ejecutarlo como administrador en VScode
3. Buscar " ;extension=fileinfo " y quitarle el ;
4. Solo debe quedar " extension=fileinfo "

## Instalar dependencias

1. **Entrar a la carpeta auth**
    Usa este comando
    ```bash
    cd auth
    ```
2. **Instala las dependencias de composer**
  ```bash
    composer install
    ```
## Iniciar servidor
    Usa este comando
    ```bash
    php artisan serve
    ```




