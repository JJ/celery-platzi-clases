#!/usr/bin/env python

# Adaptado de https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
# Con licencia libre

# Comenzar previamente con
#    celery -A PlatziTareas worker --loglevel=info

import os
import time
import re
from slackclient import SlackClient
from SlackStore import registra # Uso (encapsulado) de Celery
from dotenv import load_dotenv
load_dotenv()

slack_client = SlackClient(os.environ.get('BOT_FICHA'))
starterbot_id = None

RTM_READ_DELAY = 1 # Retraso entre lecturas del API de mensajería en tiempo real

def procesa_comandos(eventos):
    """
       Procesa una lista de comandos y devuelve orden y canal, o bien None,None
    """
    for evento in eventos:
        print(evento)
        registra.apply_async( [ evento ] ) 

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("¡Vamos charlandero!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            procesa_comandos(slack_client.rtm_read())
            time.sleep(RTM_READ_DELAY)
    else:
        print("Ha fallado. Lee más abajo para averiguar por qué")


