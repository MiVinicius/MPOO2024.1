import sys
sys.path.append('.')
import unittest
from ProjetoCadastro.Model.BaseDadosModel import BaseDadosModel, Servidor

class TestBuscarServidor(unittest.TestCase):

    def test_buscar_servidor_found(self):
        servidor = Servidor("Jurisclebson", "400.289.228-00")
        BaseDadosModel.servidores = [servidor]
        result = BaseDadosModel.buscarServidor(servidor)
        self.assertEqual(result, servidor)

    def test_buscar_servidor_not_found(self):
        servidor = Servidor("Jurisclebson", "400.289.228-00")
        BaseDadosModel.servidores = []
        result = BaseDadosModel.buscarServidor(servidor)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()