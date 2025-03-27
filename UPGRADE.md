### Instrucciones para Implementación / Deploy de la nueva versión ###

En el archivo UPGRADE se detallan los cambios a nivel configuracion y despliegue para la implementacion de la nueva version de aplicación.
Se debe implementar un UPGRADE por cada nueva version

Se deben detallar

- Cambios a nivel environment (por entorno)
- Cambios en variables de entorno
- Ejecucion de scripts de base de datos (en orden de ejecucion)
- Cambios en ejecucion de scripts y automatizaciones
- Cambios a nivel pipeline


Ejemplo:

## v1.0.0 [2024-08-01]

- Agregar nuevos parametros de configuracion en .env

QA:
APP_URL="#######'
TOKEN_URL="######"

STG:
APP_URL="#######'
TOKEN_URL="######"

PROD:
APP_URL="#######'
TOKEN_URL="######"

- Ejecutar los siguientes scripts en la base de datos para modificacion de campo / agregado de registros

QA:
script.sql

STG:
scriptq.sql

PROD:
scriptq.sql

- Agregar steps en automatizacion / pipeline

QA:
cambios.txt / .sh / .js

STG:
cambios.txt / .sh / .js

PROD:
cambios.txt / .sh / .js