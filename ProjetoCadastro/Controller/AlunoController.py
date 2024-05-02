import sys
sys.path.append('.')
from ProjetoCadastro.Model.AlunoModel import Aluno
from ProjetoCadastro.Model.BaseDadosModel import BaseDados
from ProjetoCadastro.Controller.CursoController import CursoController
from ProjetoCadastro.Model.CursoModel import Curso
from ProjetoCadastro.Controller.EnderecoController import EnderecoController
from ProjetoCadastro.Model.DisciplinaModel import Disciplina
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController

class AlunoController:
    
    @staticmethod
    def cadastrarAluno():
        nome = str(input("Digite o nome do Aluno: \n"))
        cpf = str(input("Digite o Cpf: \n"))
        aluno = Aluno(nome, cpf)
        if BaseDadosController.buscarAluno(aluno) is None:
            print("Aluno Cadastrado com sucesso!")
            BaseDadosController.cadastrarAluno(aluno)
            return True
        else:
            print("Aluno já existe!")
            return False

    @staticmethod
    def passarCurso(Aluno):
        curso = CursoController.buscarCurso(Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n"))))
        return AlunoController.buscarAluno(Aluno)._setCurso(curso)
    
    @staticmethod
    def passarDisciplina(aluno: Aluno):
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        if BaseDados.buscarDisciplina(disciplina) is None:
            print("Disciplina não existe")
            return False
        else:
            aluno._setDisciplina(disciplina)
            
    @staticmethod
    def buscarAluno():
        aluno = Aluno((str(input("Digite o nome do Aluno: \n"))), str(input("Digite o Cpf: \n")))
        return BaseDadosController.buscarAluno(aluno)
    
    @staticmethod
    def atualizarAluno():
        aluno = Aluno((str(input("Digite o nome do Aluno: \n"))), str(input("Digite o Cpf: \n")))
        novos_dados = Aluno((str(input("Digite o novo nome do Aluno: \n"))), str(input("Digite o novo Cpf: \n")), EnderecoController.cadastrarEndereco())
        return BaseDadosController.atualizarAluno(BaseDadosController.buscarAluno(aluno), novos_dados)
    
    @staticmethod
    def removerAluno():
        return BaseDadosController.deletarAluno(AlunoController.buscarAluno())
    