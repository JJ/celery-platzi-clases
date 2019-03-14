#!/usr/bin/env python


from Conexion import Conexion

canal = Conexion('../.env').canal

def callback(ch, method, properties, contenido):
    print(" [x] Recibido %r" % contenido)

canal.basic_consume(callback,
                    queue='platziq',
                    no_ack=True)

print(' [*] Esperando mensajes. Presiona CTRL+C para salir')
canal.start_consuming()
