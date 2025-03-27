# Notificación push

## Intalación


crear un _virtual enviroment_ para el proyecto de python. Se recomienda 
utilizar una versión de Python >= 3.6 

**Crear venv**

``` bash
python -m venv notificacion_push
```

**Ejecutar _virutal enviroment_**

``` bash
source virtual_enviroment/bin/activate 
```

Cargar paquetes requeridos para ejecutar el programa de notificaciones.

```
pip install -r requirements.txt
```
## Configuración

En el directorio principal de la aplicación se encuentra un archivo llamado: `conf.ini.dist`. Cópielo y renómbrelo como `conf.ini`. Dentro de este archivo va a encontrar las variables de configuración.

### Archivo conf.ini
También puede crear el archivo y agregarle el siguiente contenido:

```
[ENV]
host=https://fcm.googleapis.com/fcm/send
filename_token=tokens.txt
filename_log=logging.log
filename_csv_log=log.csv

# dry_run true no enviará las notificaciones push. false, vacío 
# o con cualquier otro valor las enviará.
dry_run=true
```

### Descripción de variables

| variable | Descripción | Valor por defecto |
|---|---|---|
| `host` | URI para la API de _Google_. | `https://fcm.googleapis.com/fcm/send` |
| `filename_token` | Ruta y nombre del archivo donde se guardan el listado de tokens. Es importante que cada token ocupen una línea de este archivo.  | `tokens_test.txt` |
| `filename_log` | Ruta y nombre del archivo donde se guarda el *log* para el módulo de _Python_: **Logging** | `loggin.log` |
| `filename_csv_log` | Ruta y nombre del archivo CSV para guardar el log de envíos asociado a cada *token*. | `log.csv` |
| `dry_run`| [`boolean`] _true_ no enviará las notificaciones mientras que: _false_, vacío o con cualquier otro valor las enviará. | `true`|

## Enviar notificaciones push

### Ayuda

Para obtener ayuda en la terminal puede ejecutar el comando `notificacion_push.py -h`. 
El resultado será el siguiente.

``` bash
Notification Push.
Usage:
    notification_push.py (--title=<title> --body=<body> --url=<url> --code=<code> --size=<size> --sleep=<sleep> --group=<group> --image=<image>)

Options:
    -h --help            Show this screen.
    -V --version         Show version.
    -t --title=<title>   Title - Título para la notificación.
    -b --body=<body>     Body - Mensaje.
    -u --url=<url>       Url - Url de destino para la notificación.
    -c --code=<code>     Code - Código de la API.
    -s --size=<size>     Size - Cantidad de token que se enviarán por lote.
    -p --sleep=<sleep>   Sleep - Tiempo de espera entre grupo de tokens.
    -g --group=<group>   Group - Grupo de tokens dentro del lote.
    -i --image=<image>   Image - URL de la imagen para la notificación.
```

## Generador de código

Para evitar errores sintácticos en el código a ejecutar desde terminal se puede utilizar el generador de código ejecutando el archivo HTML _generador.html_. Se deben completar cada uno de los campos, luego presionar el botón _enviar_ y luego hacer clic en _copiar código_. 

Pegue el código copiado en tu ventana de terminal anteponiendo el comando `python` o `python[version]` y presiona `enter`.

![Captura de pantalla del generador de código para el notificador push](assets/generador.png)

Este codigo se envia de este modo:

``` bash
python notification_push.py --title="Prueba 1.0.5" --body="Esta es una nota de prueba del día miércoles 17" --url="https://www.argentina.gob.ar/salud/mosquitos" --code="1003" --size=1 --sleep=1 --group=1 --image="https://www.argentina.gob.ar/sites/default/files/dengue-atajo-home-diciembre-2020.jpg"
```