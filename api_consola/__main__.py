# -*- coding: utf-8 -*-
from argparse import ArgumentParser

import pkg_resources

from push_notification import PushNotification
import sys

def get_version():
    version = '0.0.0'
    try:
        version = pkg_resources.require("MyProject")[0].version
    except pkg_resources.DistributionNotFound:
        pass

    line = '-' * 78
    header = f'{line}\n PUSH NOTIFICATIONS\n Version: {version}\n{line}\n'
    return header 

if __name__ == '__main__':
    parser = ArgumentParser(
        description=('Permite enviar mensajes Push a diversos dispositivos')
    )
    parser.add_argument(
        '-V',
        '--version',
        action='store_true',
        help=('Show version.')
    )
    parser.add_argument(
        '-t',
        '--title',
        type=str,
        help=('Título para la notificación.')
    )
    parser.add_argument(
        '-b',
        '--body',
        type=str,
        help=('Mensaje')
    )
    parser.add_argument(
        '-u',
        '--url',
        default='',
        type=str,
        help=('Url de destino para la notificación.')
    )
    parser.add_argument(
        '-c',
        '--code',
        default='',
        type=str,
        help=('Código de la API.')
    )
    parser.add_argument(
        '-s',
        '--size',
        default='',
        type=str,
        help=('Cantidad de token que se enviarán por lote.')
    )
    parser.add_argument(
        '-p',
        '--sleep',
        default='',
        type=str,
        help=('Tiempo de espera entre grupo de tokens.')
    )
    parser.add_argument(
        '-g',
        '--group',
        default='',
        type=str,
        help=('Grupo de tokens dentro del lote.')
    )
    parser.add_argument(
        '-i',
        '--image',
        default='',
        type=str,
        help=('URL de la imagen para la notificación.')
    )   
    # Configuración
    parser.add_argument(
        '--credentials',
        type=str,
        help=('Credenciales FireBase.')
    )
    parser.add_argument(
        '--tokens',
        type=str,
        help=('Documento con el listado de tokens')
    )
    parser.add_argument(
        '--logs-filepath',
        type=str,
        help=('Directorio donde se guardan los logs.')
    )
    args = parser.parse_args()

    if args.version:
        print(get_version())
        sys.exit(1)
    
    
    # try:
    pn = PushNotification(args.credentials, args.tokens, args.logs_filepath)
    pn.send(title=args.title,
        body=args.body,
        url=args.url,
        code=args.code,
        sleep=args.sleep,
        size=args.size,
        group=args.group,
        image=args.image)
    # except:
    #     print('Error: command invalid!')

