
from ProjetoCadastro.Model.Diretor import Diretor
from ProjetoCadastro.Model.BaseDados import BaseDados

class DiretorController:
    
    @staticmethod
    def cadastrarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        if BaseDados.buscarServidor(diretor):
            print("Diretor Cadastrado com sucesso!")
            return BaseDados.cadastrarDiretor(diretor)
        print("Diretor ja existe!")
        return False
    
    @staticmethod
    def buscarDiretor():
        return BaseDados.buscarServidor(Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n"))))
    
    @staticmethod
    def atualizarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        novos_dados = Diretor(str(input("Digite o novo nome do Diretor: \n")), str(input("Digite o novo Cpf: \n")))
        return BaseDados.atualizarServidor(DiretorController.buscarDiretor(diretor), novos_dados)
    
    @staticmethod
    def deletarDiretor():
        return BaseDados.deletarServidor(DiretorController.buscarDiretor())