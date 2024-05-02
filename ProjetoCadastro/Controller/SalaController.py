import sys
sys.path.append('.')
from ProjetoCadastro.Model.SalaModel import Sala
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController


class SalaController:
    
    @staticmethod
    def cadastrarSala():
        sala = Sala(str(input("Digite o número da sala: \n")), 
                    str(input("Digite o bloco da sala: \n")))
        return BaseDadosController.cadastrarSala(sala)
    
    @staticmethod
    def passarSala(pessoa):
        sala = Sala(str(input("Digite o número da sala: \n")), str(input("Digite o bloco da sala: \n")))
        if BaseDadosController.buscarSala(sala) is None:
            print("Sala não existe")
            return False
        else:
            pessoa._setSala(sala)
            return True 
    
    @staticmethod
    def buscarSala():
        id_sala = Sala(str(input("Digite o número da sala: \n"), str(input("Digite o bloco da sala: \n"))))
        return BaseDadosController.buscarSala(id_sala)
    
    @staticmethod
    def atualizarSala():
        sala_buscar = Sala(str(input("Digite o número da sala: \n")), str(input("Digite o bloco da sala: \n")))
        sala_nova = Sala(str(input("Digite o novo número da sala: \n")), str(input("Digite o novo bloco da sala: \n")))
        return BaseDadosController.atualizarSala(SalaController.buscarSala(sala_buscar), sala_nova)
    
    @staticmethod
    def deletarSala():
        return BaseDadosController.deletarSala(SalaController.buscarSala())
    
