import sys
sys.path.append('.')
from ProjetoCadastro.Model.Disciplina import Disciplina
from ProjetoCadastro.Model.BaseDados import BaseDados
from ProjetoCadastro.Controller.SalaController import SalaController


class DisciplinaController:
    
    @staticmethod
    def cadastrarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        return BaseDados.cadastrarDisciplina(disciplina)
    
    @staticmethod
    def passarDisciplina(pessoa):
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        return BaseDados.cadastrarDisciplina(pessoa, disciplina)
    
    @staticmethod
    def passarSala(Disciplina):
        Disciplina._setSala(SalaController.buscarSala())
    
    @staticmethod
    def buscarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")), None)
        return BaseDados.buscarDisciplina(disciplina)
    
    @staticmethod
    def atualizarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        return BaseDados.atualizarDisciplina(disciplina)
    
    @staticmethod
    def deletarDisciplina():
        return BaseDados.deletarDisciplina(DisciplinaController.buscarDisciplina())
    
    @staticmethod
    def listarDisciplinas():
        return BaseDados.listarDisciplinas()