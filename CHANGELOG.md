### Archivo de Cambios por Version ###

En este archivo CHANGELOG.md se deben indicar los cambios a nivel funcionalidad y dependencias que se han realizado en la version a desplegar, en orden en que fueron aplicados

Indicaciones

- Debe estar en la raiz del repo, no mezaclado con el codigo de la app.
- Se recomienda utilizar lenguaje Markdown.
- Se debe escribir para ser leido por seres humanos, debe ser concreto y facil de interpretar.
- Se debe generar un CHANGELOG por version a desplegar.
- Debe mostrar la fecha de publicacion de vcada version en formato yyyy-mm-dd
- Agrupar de la siguiente forma los cambios de cada version, en el orden en que figuran:


    Añadido (Added) para funcionalidades nuevas.

    Modificado (Changed) para los cambios en funcionalidades existentes.

    Obsoleto (Deprecated) para indicar que una funcionalidad está obsoleta, se queda sin soporte y se eliminará en versiones posteriores.

    Eliminado (Removed) para las funcionalidades en desuso que se eliminaron en esta versión.

    Corregido (Fixed) para corrección de errores.

    Seguridad (Security) en caso de vulnerabilidades corregidas.


Ejemplo:

## Changelog ##

## v1.0.0 [2024-08-01]

## Añadido (o Added)
- FaceID Andioid
- Face ID IOS
- Funcionalidad de Mensajeria
- Funcionalidad de Eventos
- Nuevos Estilos Agregados

## Modificado (o Changed)
- Modificacion de scripts JS
- Modificacion de estilos existentes
- Modificacion de campo en base de datos

## Obsoleto (o Deprecated)
- Version x del lenguaje pierde soporte en x fecha, se analiza modificacion en proximas versiones
- version x del framework pierde soporte en x fecha, se analiza modificacion en proxima version

## Eliminado 
- Se eliminan archivos estaticos
- Se eliminan dependencias deprecadas

## Corregido
- Se corrige error en envio de correo
- Se corrigue error en la carga de formulario

## Seguridad
- Se agrega Autenticacion doble factor
- Se ocultaron archivos de la carpeta public

