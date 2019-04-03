#!/usr/bin/env python

from Konexion import Konexion

konexion = Konexion('../.env')

konexion.productor.publish('Deskarga')

print(" [x] Solicitada descarga")
konexion.enlace.close()
