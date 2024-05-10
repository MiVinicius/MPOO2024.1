import sys
sys.path.append('.')
from ProjetoCadastro.Model.ServidorModel import Servidor
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController
from ProjetoCadastro.Controller.EnderecoController import EnderecoController

class ServidorController:
    
    @staticmethod
    def cadastrarServidor():
        servidor = Servidor((str(input("Digite o nome do Servidor: \n"))), str(input("Digite o cpf: \n")))
        if BaseDadosController.buscarServidor(servidor) is None:
            print("Servidor Cadastrado com sucesso!")
            return BaseDadosController.cadastrarServidor(servidor)
        else:
            print("Servidor ja existe!")
            return False
    
    @staticmethod
    def passarEndereco():
        return ServidorController.buscarServidor()._setEndereco(EnderecoController.cadastrarEndereco())
    
    @staticmethod
    def buscarServidor():
        servidor = Servidor((str(input("Digite o nome do Servidor: \n"))), str(input("Digite o cpf: \n")))
        return BaseDadosController.buscarServidor(servidor)
    
    @staticmethod
    def atualizarServidor():
        servidor = Servidor((str(input("Digite o nome do Servidor: \n"))), int(input("Digite o Cpf: \n")))
        novos_dados = Servidor((str(input("Digite o novo nome do Servidor: \n"))), int(input("Digite o novo Cpf: \n")))
        return BaseDadosController.atualizarServidor(ServidorController.buscarServidor(servidor), novos_dados)
        
    @staticmethod
    def removerServidor():
        return BaseDadosController.deletarServidor(ServidorController.buscarServidor())
    
    @staticmethod
    def listarServidores():
        return BaseDadosController.listarServidores()