# Guía de Commits para el Proyecto

Para mantener un historial de código limpio y trazable, es esencial seguir un estándar para los mensajes de commit. A continuación, se detallan las pautas para realizar commits en este proyecto.

## Formato Estándar de Commit

Cada commit debe seguir el siguiente formato:

\```
<opcional: gitmoji> <tipo>(<scoope>): <mensaje corto>
<opcional: línea en blanco>
<opcional: descripción detallada>
<opcional: línea en blanco>
<referencia al ID de la tarea en Jira>
\```

### Ejemplo:

\```
✨ feat(login): implementa autenticación con biometría

Se ha añadido una nueva opción de autenticación utilizando biometría. Esto proporciona una capa adicional de seguridad para los usuarios y mejora la experiencia de usuario al reducir la necesidad de introducir contraseñas.

Relacionado con el ticket JIRA-1234.
\```

## Tipos de Commit

- `feat`: Una nueva característica o funcionalidad.
- `fix`: Una corrección de bug.
- `docs`: Cambios en la documentación.
- `style`: Cambios que no afectan el significado del código (espacios en blanco, formato, etc.).
- `refactor`: Cambio en el código que no corrige un error ni añade una característica.
- `perf`: Cambios en el código que mejoran el rendimiento.
- `test`: Añadir o corregir pruebas.
- `chore`: Cambios en el proceso de construcción o herramientas auxiliares.
- `build`: Cambios que afectan al sistema de compilación o a dependencias externas (ámbitos de ejemplo: gulp, broccoli, npm).

## Gitmoji

El gitmoji es un apoyo visual referente al tipo de commit que se está realizando, cada tipo viene relacionado con un emoji
La siguiente URL proporciona los emojis dependiendo del tipo: `https://gitmoji.dev`

## Scoope

El scoope es opcional y puede referirse a la parte del código donde se realiza el cambio, como `auth api`, `cliente`, `ui`, `base de datos`,`reports api`, etc.

## Descripción Detallada

Si es necesario proporcionar más contexto o explicación sobre el commit, se puede incluir una descripción detallada después del mensaje corto.

## Referencia a Tareas

Si el commit está relacionado con una tarea específica (por ejemplo, en Jira), incluye la referencia al final del mensaje.

## Herramientas Recomendadas

- **Git (línea de comandos)**: con `git commit` y en el editor texto colocar la estructura del commit.
- **GitHub Desktop**: Ya tiene el campo summary donde deberá venir `<opcional: gitmoji> <tipo>(<scoope>): <mensaje corto>`

## Referencia

El estandar de los commits se basó en la guía que se proporciona por *Conventional Commits*
Para ver mas a detalle el estandar puedes visitar la siguiente URL: `https://www.conventionalcommits.org/en/v1.0.0/`