import os, sys, unittest
esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from PlatziAgenda import PlatziAgenda

class TestPlatziAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = PlatziAgenda()

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.agenda,PlatziAgenda, "Objeto creado correctamente")
        codigos = self.agenda.codigos()
        self.assertIsNotNone(codigos, "Hay cursos" )
        self.assertIsNotNone(self.agenda.curso( codigos[0] ), "Primer curso OK")

    def test_should_return_first_course(self):
        curso = self.agenda.siguiente()
        self.assertIsInstance( curso, dict, "Extraido primer curso" )
        self.assertNotEqual( curso['titulo'], "", "Titulo existe" )

    def test_should_return_search_result(self):
        cursos = self.agenda.busca("Curso")
        self.assertIsNotNone( cursos, "Hay algún curso")
        self.assertIn( 'titulo', cursos[list(cursos.keys())[0]], 'El curso tiene título' )
        self.assertEqual( self.agenda.busca("xyz"), { "Encontrado": None }, "Devuelve mensaje correcto")
        self.assertNotEqual( self.agenda.busca("curso"), "", "Hay algún curso" )
