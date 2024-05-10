import sys
sys.path.append('.')
from ProjetoCadastro.Model.ProfessorModel import Professor
from ProjetoCadastro.Model.CursoModel import Curso
from ProjetoCadastro.Model.DisciplinaModel import Disciplina
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController
from ProjetoCadastro.Controller.EnderecoController import EnderecoController

class ProfessorController:
    @staticmethod
    def cadastrarProfessor():
        professor = Professor(str(input("Digite o nome do Professor: \n")), str(input("Digite o cpf: \n")))
        if BaseDadosController.buscarProfessor(professor) is None:
            print("Professor Cadastrado com sucesso!")
            BaseDadosController.cadastrarProfessor(professor)
            return True
        else:
            print("Professor ja existe!")
            return False
        
    @staticmethod
    def passarEndereco():
        return ProfessorController.buscarProfessor()._setEndereco(EnderecoController.cadastrarEndereco())
        
    @staticmethod
    def passarCurso(professor: Professor):
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        if BaseDadosController.buscarCurso(curso) is None:
            print("Curso não existe")
            return False
        else:
            professor._setCurso(curso)
            return True
    
    @staticmethod
    def passarDisciplina(professor:Professor):
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        if BaseDadosController.buscarDisciplina(disciplina) is None:
            print("Disciplina não existe")
            return False
        else:
            professor._setDisciplina(disciplina)
    
    @staticmethod
    def buscarProfessor():
        professor = Professor(str(input("Digite o nome do Professor: \n")), str(input("Digite o cpf: \n")))
        return BaseDadosController.buscarProfessor(professor)
    
    @staticmethod
    def atualizarProfessor():
        professor = Professor(str(input("Digite o nome do Professor: \n")), str(input("Digite o cpf: \n")))
        novos_dados = Professor(str(input("Digite o novo nome do Professor: \n")), str(input("Digite o novo cpf: \n")))
        return BaseDadosController.atualizarProfessor(BaseDadosController.buscarProfessor(professor), novos_dados)
    
    @staticmethod
    def deletarProfessor():
        return BaseDadosController.deletarProfessor(ProfessorController.buscarProfessor())
    
    @staticmethod
    def listarProfessores():
        BaseDadosController.listarProfessores()