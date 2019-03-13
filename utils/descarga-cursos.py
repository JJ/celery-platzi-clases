#!/usr/bin/env python

"""
    Descarga los cursos de la página y los imprime en JSON en la salida estándar
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pprint
import json
import re

pp = pprint.PrettyPrinter(indent=4)
page = urlopen('http://platzi.com/agenda').read()
soup = BeautifulSoup( page, "lxml" )

agenda = soup.find_all('script')[26].text # Cambia algunas veces...

schedule = re.findall( r'scheduleItems: (.+?),\n', agenda )
datos = json.loads(schedule[0])
eventos = {}
for i in ['agenda_all','agenda_calendar']:
    for j in datos[i]['agenda_items']:
        este_dato = datos[i]['agenda_items'][j]
        eventos[ este_dato['course'] ] = { "comienzo" : este_dato['start_time'],
                                           "final" : este_dato['end_time'],
                                           "tipo": este_dato['agenda_item_type'] }
    for j in datos[i]['agenda_courses']:
        este_dato = datos[i]['agenda_courses'][j]
        course= datos[i]['agenda_courses'][j]['id']
        eventos[course]['titulo'] = este_dato['title']
        eventos[course]['URL'] = este_dato['url']
        eventos[course]['lanzamiento'] = este_dato['launch_date']

# Imprime los resultados.
print(json.dumps(eventos))
