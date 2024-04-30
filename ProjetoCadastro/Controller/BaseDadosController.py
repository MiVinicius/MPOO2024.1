import sys
sys.path.append('.')
from ProjetoCadastro.Model.BaseDados import BaseDados
class BaseDadosController:
    
    @staticmethod
    def inicializarBase():
        BaseDados.inicializarBase()
        
    @staticmethod
    def listarAlunos():
        BaseDados.listarAlunos()
        
    @staticmethod
    def listarServidores():
        BaseDados.listarServidores()
        
    @staticmethod
    def listarProfessores():
        BaseDados.listarProfessores()
        
    @staticmethod
    def listarCoordenadores():
        BaseDados.listarCoordenadores()
        
    @staticmethod
    def listarDiretores():
        BaseDados.listarDiretores()
        
    @staticmethod
    def listarCursos():
        BaseDados.listarCursos()
        
    @staticmethod
    def listarDisciplinas():
        BaseDados.listarDisciplinas()
        
    @staticmethod
    def listarSalas():
        BaseDados.listarSalas()