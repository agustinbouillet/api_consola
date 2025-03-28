import itertools
import logging
import os
import re
import time
from pathlib import Path

import firebase_admin
from firebase_admin import credentials

from api_consola.cloud_messaging import send_multicast


class PushNotification:
    def __init__(self, credentials_file:str, tokens:str, log_filepath:str):
        self.tokens = tokens
        self.credentials = credentials_file
        self.log_filepath = log_filepath
        logs_path = os.path.join(Path.cwd(), 'logs')
        self.log_filepath = log_filepath if log_filepath else logs_path
        
        if not firebase_admin._apps:
            cred = credentials.Certificate(self.credentials) 
            default_app = firebase_admin.initialize_app(cred)

        # logs configuration
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename=f'{self.log_filepath}/logs.txt', 
            level=logging.DEBUG)


    def read_ids_file(self, start:int=0, end:int=10) -> list:
        """Obtiene todos los archvos de registracion de un archivo txt.

        Abre el archivo y retorna en un listado todas las lineas contenidas en
        un rango dato en el archivo.

        Keyword Arguments:
            start {number} -- [description] (default: {0})
            end {number} -- [description] (default: {10})

        Returns:
            [list] -- Listado de registration ids.
        """
        registration_ids = []
        rgx_n = re.compile(r"\n")

        with open(self.tokens, "r") as reader:
            for r in itertools.islice(reader, start, end):
                registration_ids.append(re.sub(rgx_n, "", r))

        return registration_ids

    def send(self, **kwargs:dict):
        title = kwargs.get('title')
        body = kwargs.get('body')
        url = kwargs.get('url')
        image = kwargs.get('image')
        code = kwargs.get('code')
        sleep = kwargs.get('sleep')
        size = kwargs.get('size')
        group = kwargs.get('group')

        # Envio el post por cada grupo de ids.
        counter_lote = 1
        counter = 0

        while True:
            lote = self.read_ids_file(counter, counter + int(size))

            if lote:
                # Envia cada uno de los lotes sin tiempo de espera hasta que el
                # contador llegue al numero n especificado en los 
                # argumentos. Entonces hace un sleep.
                send_multicast( 
                    f'{self.log_filepath}/log-conections.txt', 
                    lote,
                    title=title, 
                    body=body, 
                    url=url, 
                    code=code, 
                    registration_ids=lote, 
                    image=image)

                # Registro los envios.
                logging.info(f"ENVIADO: range({counter}, {counter + int(size)})")

                if counter_lote == int(group):
                    time.sleep(int(sleep))
                    counter_lote = 0

                counter += int(size)
                counter_lote += 1
            else:
                break