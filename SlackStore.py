import os
from celery import Celery,task
from dotenv import load_dotenv
import sqlite3
import datetime
import json


load_dotenv()

app = Celery('slack-store',
             broker='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')))

now = datetime.datetime.now()
registro = sqlite3.connect("registro-{}-{}-{}-{}-{}.db".format(now.year,now.month, now.day, now.hour, now.minute))
registro.execute('''CREATE TABLE  IF NOT EXISTS mensajes
                    (fecha text, texto text)''')

@app.task
def registra(evento):
    print(json.dumps(evento))
    mensaje = ''
    if 'content' in evento:
        mensaje = "Mensaje A → {}".format( evento['content'] ) 
    elif 'text' in evento:
        mensaje = "Mensaje B → {}".format( evento['text'] ) 
    else:
        mensaje = "Info → {}".format( evento['type'] )

    for x in range(0,30):
        try:
            with registro:
                registro.execute( "INSERT INTO mensajes VALUES( \"{}\",\"{}\" )".format( datetime.datetime.now(), mensaje ) )
        except:
            time.sleep(1)
            pass
        finally:
            break
    else:
        with connection:
            connection.execute(sql)  

@app.task
def cuantos(quien):
    print("Quien : ", quien)
    with registro:
        resultado = registro.execute( "select COUNT(*) from mensajes where texto like \"Mensaje B → %{}%\"".format( quien ) ).fetchall()
        print("Buscando ", quien, " → ", resultado)
        return resultado
