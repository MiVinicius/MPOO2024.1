from Model.BaseDados import BaseDados
# from Model.Aluno import Aluno
from Controller.AlunoController import AlunoController
BaseDados()
BaseDados.inicializarBase()
BaseDados.listarAlunos()
AlunoController.cadastrarAluno()
# aluno = Aluno("Elias", "426.272.465.04")
# print(baseDados.cadastrarAluno(aluno))
# print(baseDados.buscarAluno(aluno))
BaseDados.listarAlunos()
print(BaseDados.alunos[2]._getNome())