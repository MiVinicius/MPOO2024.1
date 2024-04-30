import sys
sys.path.append('.')
from ProjetoCadastro.Model.Curso import Curso
from ProjetoCadastro.Model.BaseDados import BaseDados
from ProjetoCadastro.Model.Coordenador import Coordenador

class CursoController:
    
    @staticmethod
    def cadastrarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")),
                    str(input("Digite o período do curso: \n")))
        if BaseDados.buscarCurso() is None:
            print("Curso cadastrado com sucesso!")
            return BaseDados.cadastrarCurso(curso)
        else:
            print("Curso ja existe!")
            return False
    @staticmethod
    def passarCoordenador(curso:Curso):
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        if BaseDados.buscarServidor(coordenador) is None:
            print("Coordenador não existe!")
            return False
        else:
            curso._setCoordenador(coordenador)
    @staticmethod
    def buscarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        return BaseDados.buscarCurso(curso)
    
    @staticmethod
    def atualizarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        novos_dados = Curso(str(input("Digite o novo nome do curso: \n")), str(input("Digite o novo período do curso: \n")))
        return BaseDados.atualizarCurso(BaseDados.buscarCurso(curso), novos_dados) 
        
    @staticmethod
    def removerCurso():
        return BaseDados.deletarCurso(CursoController.buscarCurso())
    
    @staticmethod
    def listarCursos():
        return BaseDados.listarCursos()