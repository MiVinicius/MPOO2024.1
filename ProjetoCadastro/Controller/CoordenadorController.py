import sys
sys.path.append('.')
from ProjetoCadastro.Model.CoordenadorModel import Coordenador
from ProjetoCadastro.Model.CursoModel import Curso
from ProjetoCadastro.Controller.CursoController import CursoController
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController
from ProjetoCadastro.Controller.EnderecoController import EnderecoController

class CoordenadorController:
    @staticmethod
    def cadastrarCoordenador():
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        if BaseDadosController.buscarCoordenador(coordenador) is None:
            print("Coordenador Cadastrado com sucesso!")
            BaseDadosController.cadastrarCoordenador(coordenador)
            return True 
        else:
            print("Coordenador ja existe!")
            return False
    
    @staticmethod
    def passarEndereco(Coordenador):
        return CoordenadorController.buscarCoordenador(Coordenador)._setEndereco(EnderecoController.cadastrarEndereco())
    
    @staticmethod
    def passarCurso(Coordenador):
        curso = CursoController.buscarCurso(Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n"))))
        return CoordenadorController.buscarCoordenador(Coordenador)._setCurso(curso)
    
    @staticmethod
    def buscarCoordenador():
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        return BaseDadosController.buscarCoordenador(coordenador)
    
    @staticmethod
    def atualizarCoordenador():
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        novos_dados = Coordenador((str(input("Digite o novo nome do Coordenador: \n"))), str(input("Digite o novo Cpf: \n")))
        return BaseDadosController.atualizarCoordenador(BaseDadosController.buscarCoordenador(coordenador), novos_dados)
    
    @staticmethod
    def removerCoordenador():
        return BaseDadosController.deletarCoordenador(CoordenadorController.buscarCoordenador())
    