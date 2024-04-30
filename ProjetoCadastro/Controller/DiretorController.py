import sys
sys.path.append('.')
from ProjetoCadastro.Model.Diretor import Diretor
from ProjetoCadastro.Model.BaseDados import BaseDados

class DiretorController:
    
    @staticmethod
    def cadastrarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        if BaseDados.buscarServidor(diretor):
            print("Diretor Cadastrado com sucesso!")
            BaseDados.cadastrarDiretor(diretor)
            return True
        else:
            print("Diretor ja existe!")
            return False
    
    @staticmethod
    def buscarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        return BaseDados.buscarServidor(diretor)
    
    @staticmethod
    def atualizarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        novos_dados = Diretor(str(input("Digite o novo nome do Diretor: \n")), str(input("Digite o novo Cpf: \n")))
        return BaseDados.atualizarServidor(DiretorController.buscarDiretor(diretor), novos_dados)
    
    @staticmethod
    def deletarDiretor():
        return BaseDados.deletarServidor(DiretorController.buscarDiretor())