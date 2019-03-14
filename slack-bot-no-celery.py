#!/usr/bin/env python

# Adaptado de https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
# Debe tener licencia libre

import os
import time
import re
from slackclient import SlackClient
from PlatziAgenda import PlatziAgenda
from SlackComandos import SlackComandos

from PlatziSlack import PlatziSlackComando

from dotenv import load_dotenv
load_dotenv()

slack_client = SlackClient(os.environ.get('BOT_FICHA'))
starterbot_id = None

RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENCION_REGEX = "^<@(|[WU].+?)>(.*)"

# Define los comandos
comandos = SlackComandos()

def ve(*args):
    return "Por lo pronto vas bien"

def siguiente(agenda,*args):
    siguiente = agenda.siguiente()
    return "El siguiente curso es *{}*".format(siguiente['titulo'])

def busca(agenda, argumento ):
    resultado = agenda.busca( argumento )
    response = "Tenemos los siguientes cursos\n"
    for i in resultado:
        response = response + "→ " + resultado[i]['titulo']+"\n"
    return response

PlatziSlackComando( comandos, "ve", ve )
PlatziSlackComando( comandos, "siguiente", siguiente )
PlatziSlackComando( comandos, "busca", busca )

def procesa_comandos(eventos):
    """
       Procesa una lista de comandos y devuelve orden y canal, o bien None,None
    """
    for evento in eventos:
        if evento["type"] == "message" and not "subtype" in evento:
            user_id, message = procesa_mencion_directa(evento["text"])
            if user_id == starterbot_id:
                return message, evento["channel"]
    return None, None

def procesa_mencion_directa(texto):
    """
        Encuentra menciones directas y devuelve el ID mencionado o nada.
    """
    matches = re.search(MENCION_REGEX, texto)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def maneja_comando(comando, canal):
    """
        Ejecuta el comando si se conoce.
    """
    # Default response is help text for the user
    default_response = "No te entiendo. Prueba *ve*."

    response = comandos.maneja( comando )

    slack_client.api_call(
        "chat.postMessage",
        channel=canal,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("¡Vamos charlandero!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = procesa_comandos(slack_client.rtm_read())
            if command:
                maneja_comando(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Ha fallado. Lee más abajo para averiguar por qué")


