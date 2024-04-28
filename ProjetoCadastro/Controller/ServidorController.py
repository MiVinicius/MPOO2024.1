
from ProjetoCadastro.Model.Servidor import Servidor
from ProjetoCadastro.Model.BaseDados import BaseDados

class ServidorController:
    
    @staticmethod
    def cadastrarServidor():
        servidor = Servidor((str(input("Digite o nome do Servidor: \n"))), str(input("Digite o cpf: \n")))
        if BaseDados.buscarServidor(servidor) is None:
            print("Servidor Cadastrado com sucesso!")
            return BaseDados.cadastrarServidor(servidor)
        print("Servidor ja existe!")
        return False
    
    @staticmethod
    def buscarServidor():
        return BaseDados.buscarServidor(Servidor((str(input("Digite o nome do Servidor: \n"))), str(input("Digite o cpf: \n"))))
    
    @staticmethod
    def atualizarServidor():
        servidor = Servidor((str(input("Digite o nome do Servidor: \n"))), int(input("Digite o Cpf: \n")))
        novos_dados = Servidor((str(input("Digite o novo nome do Servidor: \n"))), int(input("Digite o novo Cpf: \n")))
        return BaseDados.atualizarServidor(ServidorController.buscarServidor(servidor), novos_dados)
        
    @staticmethod
    def removerServidor():
        return BaseDados.deletarServidor(ServidorController.buscarServidor())