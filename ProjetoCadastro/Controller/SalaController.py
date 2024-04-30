import sys
sys.path.append('.')
from ProjetoCadastro.Model.Sala import Sala
from ProjetoCadastro.Model.BaseDados import BaseDados


class SalaController:
    
    @staticmethod
    def cadastrarSala():
        sala = Sala(str(input("Digite o número da sala: \n")), 
                    str(input("Digite o bloco da sala: \n")))
        return BaseDados.cadastrarSala(sala)
    
    @staticmethod
    def passarSala(pessoa):
        sala = Sala(str(input("Digite o número da sala: \n")), str(input("Digite o bloco da sala: \n")))
        return BaseDados.cadastrarSala(BaseDados.buscarSala(sala), pessoa)
    
    @staticmethod
    def buscarSala():
        id_sala = Sala(str(input("Digite o número da sala: \n"), str(input("Digite o bloco da sala: \n"))))
        return BaseDados.buscarSala(id_sala)
    
    @staticmethod
    def atualizarSala():
        sala_buscar = Sala(str(input("Digite o número da sala: \n")), str(input("Digite o bloco da sala: \n")))
        sala_nova = Sala(str(input("Digite o novo número da sala: \n")), str(input("Digite o novo bloco da sala: \n")))
        return BaseDados.atualizarSala(SalaController.buscarSala(sala_buscar), sala_nova)
    
    @staticmethod
    def deletarSala():
        return BaseDados.deletarSala(SalaController.buscarSala())
    
    @staticmethod
    def listarSalas():
        return BaseDados.listarSalas()