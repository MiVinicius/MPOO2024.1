import sys
sys.path.append('.')
from ProjetoCadastro.Model.Professor import Professor
from ProjetoCadastro.Model.BaseDados import BaseDados
from ProjetoCadastro.Model.Curso import Curso

class ProfessorController:
    @staticmethod
    def cadastrarProfessor():
        professor = Professor(str(input("Digite o nome do Professor: \n")), str(input("Digite o cpf: \n")))
        if BaseDados.buscarServidor(professor) is None:
            print("Professor Cadastrado com sucesso!")
            BaseDados.cadastrarProfessor(professor)
            return True
        else:
            print("Professor ja existe!")
            return False
    
    def passarCurso(Professor):
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        return ProfessorController.buscarProfessor(Professor)._setCurso(curso)
    
    @staticmethod
    def buscarProfessor():
        professor = Professor(str(input("Digite o nome do Professor: \n")), str(input("Digite o cpf: \n")))
        return BaseDados.buscarServidor(professor)
    
    @staticmethod
    def atualizarProfessor():
        professor = Professor(str(input("Digite o nome do Professor: \n")), str(input("Digite o cpf: \n")))
        novos_dados = Professor(str(input("Digite o novo nome do Professor: \n")), str(input("Digite o novo cpf: \n")))
        return BaseDados.atualizarServidor(BaseDados.buscarServidor(professor), novos_dados)
    
    @staticmethod
    def deletarProfessor():
        return BaseDados.deletarServidor(ProfessorController.buscarProfessor())