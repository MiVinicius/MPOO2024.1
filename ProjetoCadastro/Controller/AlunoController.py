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
        try:  
            aluno = Aluno((str(input("Digite o nome do Aluno: \n"))), int(input("Digite o Cpf: \n")))
            if BaseDados.buscarAluno(aluno) is None:
                print("Aluno Cadastrado com sucesso!")
                return BaseDados.cadastrarAluno(aluno)
            print("Aluno ja existe!")
            return False
        except TypeError:
            print("Erro de tipo de input de dado!")
            BaseDados.cadastrarAluno()
        except ValueError:
            print("erro de valor do input de dado")
            BaseDados.cadastrarAluno()
            
    @staticmethod
    def passarCurso(Aluno):
        curso = CursoController.buscarCurso(Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n"))))
        return AlunoController.buscarAluno(Aluno)._setCurso(curso)
            
    @staticmethod
    def buscarAluno():
        return BaseDados.buscarAluno(Aluno((str(input("Digite o nome do Aluno: \n"))), int(input("Digite o Cpf: \n"))))
    
    @staticmethod
    def atualizarAluno():
        aluno = Aluno((str(input("Digite o nome do Aluno: \n"))), int(input("Digite o Cpf: \n")))
        novos_dados = Aluno((str(input("Digite o novo nome do Aluno: \n"))), int(input("Digite o novo Cpf: \n")), EnderecoController.cadastrarEndereco())
        return BaseDados.atualizarAluno(BaseDados.buscarAluno(aluno), novos_dados)
    
    @staticmethod
    def removerAluno():
        return BaseDados.deletarAluno(AlunoController.buscarAluno())
    