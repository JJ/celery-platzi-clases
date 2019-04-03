#!/usr/bin/env python

from kombu import Connection, Exchange, Producer, Queue
import os
from dotenv import load_dotenv

class Konexion:
    """Encapsula la conexión a RabbitMQ usando Kombu"""
    
    enlace    = None
    canal     = None
    estafeta  = None
    productor = None
    cola      = None
    
    def __init__( self, dotenv_path=".env" ):
        load_dotenv(dotenv_path=dotenv_path)

        url = 'amqp://{}:{}@localhost:5672/platziv'.format(os.environ.get('TEST_USER'),os.environ.get('TEST_PASS'))

        self.enlace = Connection( url )
        self.canal = self.enlace.channel()
#        self.estafeta = Exchange("platzie", type="direct")
        self.estafeta = Exchange("", type="direct")
        self.productor = Producer(exchange=self.estafeta, channel=self.canal, routing_key="platziq")
        self.cola = Queue(name="platziq", exchange=self.estafeta, routing_key="platziq") 
        self.cola.maybe_bind( self.enlace )
    
