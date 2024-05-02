import sys
sys.path.append('.')
from ProjetoCadastro.Model.CursoModel import Curso
from ProjetoCadastro.Model.CoordenadorModel import Coordenador
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController

class CursoController:
    
    @staticmethod
    def cadastrarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")),
                    str(input("Digite o período do curso: \n")))
        if BaseDadosController.buscarCurso() is None:
            print("Curso cadastrado com sucesso!")
            return BaseDadosController.cadastrarCurso(curso)
        else:
            print("Curso ja existe!")
            return False
    @staticmethod
    def passarCoordenador(curso:Curso):
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        if BaseDadosController.buscarCoordenador(coordenador) is None:
            print("Coordenador não existe!")
            return False
        else:
            curso._setCoordenador(coordenador)
    @staticmethod
    def buscarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        return BaseDadosController.buscarCurso(curso)
    
    @staticmethod
    def atualizarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        novos_dados = Curso(str(input("Digite o novo nome do curso: \n")), str(input("Digite o novo período do curso: \n")))
        return BaseDadosController.atualizarCurso(BaseDadosController.buscarCurso(curso), novos_dados) 
        
    @staticmethod
    def removerCurso():
        return BaseDadosController.deletarCurso(CursoController.buscarCurso())
    
