import sys
sys.path.append('.')
from ProjetoCadastro.Model.Disciplina import Disciplina
from ProjetoCadastro.Model.BaseDados import BaseDados
from ProjetoCadastro.Model.Curso import Curso
from ProjetoCadastro.Model.Sala import Sala

class DisciplinaController:
    
    @staticmethod
    def cadastrarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        return BaseDados.cadastrarDisciplina(disciplina)
    
    @staticmethod
    def passarDisciplina(disciplina: Disciplina):
        curso = Curso(str(input("Digite o nome da disciplina: \n")))
        if BaseDados.buscarCurso(curso) is None:
            print("Disciplina não existe")
            return False
        else:
            curso._setDisciplina(disciplina)
            return True
    
    @staticmethod
    def passarSala(disciplina:Disciplina):
        sala = Sala(str(input("Digite o nome da disciplina: \n")), int(input("Digite o bloco da disciplina: \n")))
        if BaseDados.buscarSala(sala) is None:
            print("Sala não existe")
            return False
        else:
            disciplina._setSala(sala)
            return True
    
    @staticmethod
    def buscarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")), None)
        return BaseDados.buscarDisciplina(disciplina)
    
    @staticmethod
    def atualizarDisciplina():
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")))
        novos_dados = Disciplina(str(input("Digite o novo nome da disciplina: \n")))
        return BaseDados.atualizarDisciplina(disciplina, novos_dados)
    
    @staticmethod
    def deletarDisciplina():
        return BaseDados.deletarDisciplina(DisciplinaController.buscarDisciplina())
    
    @staticmethod
    def listarDisciplinas():
        return BaseDados.listarDisciplinas()