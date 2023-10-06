# Reports API con Flask

Este proyecto es una API desarrollada con Flask. A continuación, se detallan los pasos para configurar y ejecutar el proyecto.

## Pre-requisitos

1. **Python**: Asegúrate de tener instalada la versión 3.8.0 o una compatible. Puedes verificar tu versión con el siguiente comando:
    ```bash
    python --version
    ```

2. **pip**: Es necesario contar con pip para instalar las dependencias. Verifica que lo tienes instalado con:
    ```bash
    pip --version
    ```

## Configuración del entorno

1. **Instalación de virtualenv**: Si no tienes `virtualenv` instalado, puedes hacerlo con el siguiente comando:
    ```bash
    pip install virtualenv
    ```

2. **Creación del entorno virtual**: Navega a la raíz de la carpeta "reports" y crea un entorno virtual con el nombre `vc_venv`:
    ```bash
    cd reports
    virtualenv vc_venv
    ```

3. **Activación del entorno virtual**: Una vez creado el entorno virtual, actívalo con el siguiente comando:
    ```bash
    .\vc_venv\Scripts\activate
    ```

4. **Instalación de dependencias**: Con el entorno virtual activado, instala las dependencias del proyecto:
    ```bash
    pip install -r ./requirements.txt
    ```

5. **Verificación de dependencias**: Puedes verificar que las dependencias se hayan instalado correctamente con:
    ```bash
    pip freeze
    ```

## Ejecución del servidor

Para iniciar el servidor de *Reports API*, ejecuta el siguiente comando:

```bash
python .\APP_VZCDNA.py
