import sys
sys.path.append('.')
from ProjetoCadastro.Model.Aluno import Aluno
from ProjetoCadastro.Model.BaseDados import BaseDados
from ProjetoCadastro.Controller.CursoController import CursoController
from ProjetoCadastro.Model.Curso import Curso
from ProjetoCadastro.Controller.EnderecoController import EnderecoController

class AlunoController:
    
    @staticmethod
    def cadastrarAluno():
        nome = str(input("Digite o nome do Aluno: \n"))
        cpf = str(input("Digite o Cpf: \n"))
        aluno = Aluno(nome, cpf)
        if BaseDados.buscarAluno(aluno) is None:
            print("Aluno Cadastrado com sucesso!")
            BaseDados.cadastrarAluno(aluno)
            return True
        else:
            print("Aluno já existe!")
            return False


    @staticmethod
    def passarCurso(Aluno):
        curso = CursoController.buscarCurso(Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n"))))
        return AlunoController.buscarAluno(Aluno)._setCurso(curso)
            
    @staticmethod
    def buscarAluno():
        aluno = Aluno((str(input("Digite o nome do Aluno: \n"))), str(input("Digite o Cpf: \n")))
        return BaseDados.buscarAluno(aluno)
    
    @staticmethod
    def atualizarAluno():
        aluno = Aluno((str(input("Digite o nome do Aluno: \n"))), str(input("Digite o Cpf: \n")))
        novos_dados = Aluno((str(input("Digite o novo nome do Aluno: \n"))), str(input("Digite o novo Cpf: \n")), EnderecoController.cadastrarEndereco())
        return BaseDados.atualizarAluno(BaseDados.buscarAluno(aluno), novos_dados)
    
    @staticmethod
    def removerAluno():
        return BaseDados.deletarAluno(AlunoController.buscarAluno())
    