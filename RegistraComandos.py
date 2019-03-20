import os
from celery import Celery,shared_task
from dotenv import load_dotenv
import datetime
import sqlite3
import json


load_dotenv()

app = Celery('registra-comandos',
             broker='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')))

now = datetime.datetime.now()
registro = sqlite3.connect("comandos-{}-{}-{}-{}-{}.db".format(now.year,now.month, now.day, now.hour, now.minute))
registro.execute('''CREATE TABLE  IF NOT EXISTS registro
                    (repeticiones INT, comando VARCHAR(32) unique )''')

@shared_task
def registra(comando):
    print(json.dumps(comando))
    cuantos=0
    with registro:
        resultado = registro.execute( "SELECT repeticiones FROM REGISTRO where comando = \"{}\"".format( comando ) ).fetchall()
        print( "Resultado ", resultado )
        if resultado:
            cuantos = resultado[0][0]
        
    print("Comandos {} → {}".format( comando, cuantos ))
    
    for x in range(0,30):
        try:
            with registro:
                registro.execute( "INSERT OR REPLACE INTO registro (repeticiones, comando) VALUES( {},\"{}\" );".format( cuantos+1, comando ))
        except:
            time.sleep(1)
            pass
        finally:
            break

