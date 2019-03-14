import os, sys, unittest
esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from SlackComandos import SlackComandos
from PlatziSlack import PlatziSlackComando


class TestPlatziSlackComando(unittest.TestCase):

    def setUp(self):
        self.comandos = SlackComandos()

    def test_should_initialize_object_OK(self):
        hola = lambda x: "Hola"
        PlatziSlackComando( self.comandos, "Hola", hola)

