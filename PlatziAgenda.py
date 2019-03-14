import os, json, re

class PlatziAgenda:
# 'Una clase para contener los elementos de la agenda de la web de Platzi

    def __init__ (self,  data_file = "data/cursos.json"):
#  Inicializa con el nombre del fichero extraído por scraping
        if not os.path.exists( data_file ):
            data_file = "../" + data_file

        with open(data_file) as f:
            self.agenda = json.load(f)
            self.primero = sorted(self.agenda.keys())[0]

    def siguiente(self):
#    Devuelve el curso siguiente, buscando por índice
        return self.agenda[self.primero]

    def codigos(self): # Devuelve todos los códigos que hay ahora mismo
        return list(self.agenda.keys())

    def curso(self, codigo ): #  Devuelve el curso correspondiente al código
        return self.agenda[codigo]

    def busca(self, aguja ):
#  Devuelve los cursos que incluyen esa cadena en el título, indexados por código de curso, o "Resultado: None" en caso de que no haya ninguno.
        resultado = {}
        for k, v in self.agenda.items():
            if v['titulo'].lower().find( aguja.lower() ) >= 0:
                resultado[k]= v

        if not resultado:
            resultado = { "Encontrado": None }

        return resultado



