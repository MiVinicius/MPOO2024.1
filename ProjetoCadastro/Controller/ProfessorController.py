import sys
sys.path.append('.')
from ProjetoCadastro.Model.Professor import Professor
from ProjetoCadastro.Model.BaseDados import BaseDados
from ProjetoCadastro.Model.Curso import Curso
from ProjetoCadastro.Model.Disciplina import Disciplina

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
    @staticmethod
    def passarCurso(professor: Professor):
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        if BaseDados.buscarCurso(curso) is None:
            print("Curso não existe")
            return False
        else:
            professor._setCurso(curso)
            return True
    
    @staticmethod
    def passarDisciplina(professor:Professor):
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        if BaseDados.buscarDisciplina(disciplina) is None:
            print("Disciplina não existe")
            return False
        else:
            professor._setDisciplina(disciplina)
    
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