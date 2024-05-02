import sys
sys.path.append('.')
from ProjetoCadastro.Model.DisciplinaModel import Disciplina
from ProjetoCadastro.Model.CursoModel import Curso
from ProjetoCadastro.Model.SalaModel import Sala
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController

class DisciplinaController:
    
    @staticmethod
    def cadastrarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        return BaseDadosController.cadastrarDisciplina(disciplina)
    
    @staticmethod
    def passarDisciplina(disciplina: Disciplina):
        curso = Curso(str(input("Digite o nome da disciplina: \n")))
        if BaseDadosController.buscarCurso(curso) is None:
            print("Disciplina não existe")
            return False
        else:
            curso._setDisciplina(disciplina)
            return True
    
    @staticmethod
    def passarSala(disciplina:Disciplina):
        sala = Sala(str(input("Digite o nome da disciplina: \n")), int(input("Digite o bloco da disciplina: \n")))
        if BaseDadosController.buscarSala(sala) is None:
            print("Sala não existe")
            return False
        else:
            disciplina._setSala(sala)
            return True
    
    @staticmethod
    def buscarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")), None)
        return BaseDadosController.buscarDisciplina(disciplina)
    
    @staticmethod
    def atualizarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        novos_dados = Disciplina(str(input("Digite o novo nome da disciplina: \n")))
        return BaseDadosController.atualizarDisciplina(disciplina, novos_dados)
    
    @staticmethod
    def deletarDisciplina():
        return BaseDadosController.deletarDisciplina(DisciplinaController.buscarDisciplina())
    
