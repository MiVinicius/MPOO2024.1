import sys
sys.path.append('.')
from ProjetoCadastro.Model.Coordenador import Coordenador
from ProjetoCadastro.Model.BaseDados import BaseDados
from ProjetoCadastro.Model.Curso import Curso
from ProjetoCadastro.Controller.CursoController import CursoController

class CoordenadorController:
    @staticmethod
    def cadastrarCoordenador():
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        if BaseDados.buscarServidor(coordenador) is None:
            print("Coordenador Cadastrado com sucesso!")
            BaseDados.cadastrarCoordenador(coordenador)
            return True 
        else:
            print("Coordenador ja existe!")
            return False
    
    @staticmethod
    def passarCurso(Coordenador):
        curso = CursoController.buscarCurso(Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n"))))
        return CoordenadorController.buscarCoordenador(Coordenador)._setCurso(curso)
    
    @staticmethod
    def buscarCoordenador():
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        return BaseDados.buscarServidor(coordenador)
    
    @staticmethod
    def atualizarCoordenador():
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        novos_dados = Coordenador((str(input("Digite o novo nome do Coordenador: \n"))), str(input("Digite o novo Cpf: \n")))
        return BaseDados.atualizarServidor(BaseDados.buscarServidor(coordenador), novos_dados)
    
    @staticmethod
    def removerCoordenador():
        return BaseDados.deletarServidor(CoordenadorController.buscarCoordenador())
    