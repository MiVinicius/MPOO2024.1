import sys
sys.path.append('.')
from ProjetoCadastro.Model.BaseDadosModel import BaseDadosModel
# from Model.Aluno import Aluno
from Controller.AlunoController import AlunoController
BaseDadosModel()
# BaseDados._inicializarBase()
BaseDadosModel.listarAlunos()
AlunoController.cadastrarAluno()
# aluno = Aluno("Elias", "426.272.465.04")
# print(baseDados.cadastrarAluno(aluno))
# print(baseDados.buscarAluno(aluno))
BaseDadosModel.listarAlunos()
print(BaseDadosModel.alunos[2]._getNome())