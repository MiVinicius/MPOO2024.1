import sys
sys.path.append('.')
from ProjetoCadastro.Model.DiretorModel import Diretor
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController
from ProjetoCadastro.Controller.EnderecoController import EnderecoController

class DiretorController:
    
    @staticmethod
    def cadastrarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        if BaseDadosController.buscarDiretor(diretor):
            print("Diretor Cadastrado com sucesso!")
            BaseDadosController.cadastrarDiretor(diretor)
            return True
        else:
            print("Diretor ja existe!")
            return False
    
    @staticmethod
    def passarEndereco():
        return DiretorController.buscarDiretor()._setEndereco(EnderecoController.cadastrarEndereco())
    
    @staticmethod
    def buscarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        return BaseDadosController.buscarDiretor(diretor)
    
    @staticmethod
    def atualizarDiretor():
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        novos_dados = Diretor(str(input("Digite o novo nome do Diretor: \n")), str(input("Digite o novo Cpf: \n")))
        return BaseDadosController.atualizarDiretor(DiretorController.buscarDiretor(diretor), novos_dados)
    
    @staticmethod
    def deletarDiretor():
        return BaseDadosController.deletarDiretor(DiretorController.buscarDiretor())
    
    @staticmethod
    def listarDiretor():
        return BaseDadosController.listarDiretores()