import os
from PlatziAgenda import PlatziAgenda
from celery import Celery,task
from dotenv import load_dotenv
import socket


load_dotenv()
hostname = socket.gethostname()
url = 'amqp://platzi:{}@{}/platzi'.format(os.environ.get('RMQ_PASS'),hostname)
app = Celery('platzi-tareas', broker=url, backend=url )

@app.task
def siguiente():
    agenda = PlatziAgenda()
    return agenda.siguiente()

@app.task
def busca( argumento ):
    agenda = PlatziAgenda()
    resultado = agenda.busca( argumento )
    response = ""
    if not "Encontrado" in resultado: 
        response = "Tenemos los siguientes cursos\n"
        for i in resultado:
            response = response + "→ " + resultado[i]['titulo']+"\n"
    else:
        response = "Lo siento: no hay ningún curso con *{}*\n".format(argumento)

    return response
