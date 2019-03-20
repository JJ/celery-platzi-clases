#!/usr/bin/env python

# Adaptado de https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
# Con licencia libre

# Comenzar previamente con
#    celery -A PlatziTareas worker --loglevel=info

import os
import time
import re

from celery import Celery
from slackclient import SlackClient
from SlackStore import registra # Uso (encapsulado) de Celery
from cuentacomandos import cuenta
from dotenv import load_dotenv
from kombu import Queue

load_dotenv()

slack_client = SlackClient(os.environ.get('BOT_FICHA'))
starterbot_id = None

RTM_READ_DELAY = 1 # Retraso entre lecturas del API de mensajería en tiempo real
MENCION_REGEX = "^<@(|[WU].+?)>(.*)" # Expresión regular para detectar llamadas bot


#Definiendo encaminado
app = Celery('client',
             broker='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')))

app.conf.task_default_queue = 'rutauno'
app.conf.task_queues = (
    Queue('rutauno',routing_key='guarda.#'),
    Queue('ruta33', routing_key='cuenta.#'),
)


def procesa_mencion_directa(texto):
    """
        Encuentra menciones directas y devuelve el ID mencionado o nada.
    """
    matches = re.search(MENCION_REGEX, texto)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def procesa_comandos(eventos):
    """
       Procesa una lista de comandos y devuelve orden y canal, o bien None,None
    """
    for evento in eventos:
        registra.apply_async( [evento],
                              queue = 'rutauno',
                              routing_key = 'guarda.comandos' ) 
        if evento["type"] == "message" and not "subtype" in evento:
            user_id, message = procesa_mencion_directa(evento["text"])
            if user_id == starterbot_id:
                cuenta.apply_async( [message.split(" ")[0]],
                                    queue = 'ruta33',
                                    routing_key = 'cuenta.comandos' )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("¡Vamos charlandero!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            procesa_comandos(slack_client.rtm_read())
            time.sleep(RTM_READ_DELAY)
    else:
        print("Ha fallado. Lee más abajo para averiguar por qué")


