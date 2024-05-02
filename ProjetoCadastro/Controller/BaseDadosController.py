import sys
sys.path.append('.')
from ProjetoCadastro.Model.BaseDadosModel import BaseDados
class BaseDadosController:
    
    @staticmethod
    def inicializarBase():
        BaseDados._inicializarBase()
        
    @staticmethod
    def cadastrarAluno(aluno):
        return BaseDados.cadastrarAluno(aluno)
        
    @staticmethod
    def buscarAluno(aluno):
        return BaseDados.buscarAluno(aluno)
    
    @staticmethod
    def atualizarAluno(aluno, novos_dados):
        return BaseDados.atualizarAluno(aluno, novos_dados)
    
    @staticmethod
    def deletarAluno(aluno):
        return BaseDados.deletarAluno(aluno)
    
    @staticmethod
    def cadastrarServidor(servidor):
        return BaseDados.cadastrarServidor(servidor)
    
    @staticmethod
    def buscarServidor(servidor):
        return BaseDados.buscarServidor(servidor)
    
    @staticmethod
    def atualizarServidor(servidor, novos_dados):
        return BaseDados.atualizarServidor(servidor, novos_dados)
    
    @staticmethod
    def deletarServidor(servidor):
        return BaseDados.deletarServidor(servidor)
    
    @staticmethod
    def cadastrarProfessor(professor):
        return BaseDados.cadastrarProfessor(professor)
    
    @staticmethod
    def buscarProfessor(professor):
        return BaseDados.buscarProfessor(professor)
    
    @staticmethod
    def atualizarProfessor(professor, novos_dados):
        return BaseDados.atualizarProfessor(professor, novos_dados)
    
    @staticmethod
    def deletarProfessor(professor):
        return BaseDados.deletarProfessor(professor)
    
    @staticmethod
    def cadastrarCoordenador(coordenador):
        return BaseDados.cadastrarCoordenador(coordenador)
    
    @staticmethod
    def buscarCoordenador(coordenador):
        return BaseDados.buscarCoordenador(coordenador)
    
    @staticmethod
    def atualizarCoordenador(coordenador, novos_dados):
        return BaseDados.atualizarCoordenador(coordenador, novos_dados)
    
    @staticmethod
    def deletarCoordenador(coordenador):
        return BaseDados.deletarCoordenador(coordenador)
    
    @staticmethod
    def cadastrarDiretor(diretor):
        return BaseDados.cadastrarDiretor(diretor)
    
    @staticmethod
    def buscarDiretor(diretor):
        return BaseDados.buscarDiretor(diretor)
    
    @staticmethod
    def atualizarDiretor(diretor, novos_dados):
        return BaseDados.atualizarDiretor(diretor, novos_dados)
    
    @staticmethod
    def deletarDiretor(diretor):
        return BaseDados.deletarDiretor(diretor)
    
    @staticmethod
    def cadastrarCurso(curso):
        return BaseDados.cadastrarCurso(curso)
    
    @staticmethod
    def buscarCurso(curso):
        return BaseDados.buscarCurso(curso)
    
    @staticmethod
    def atualizarCurso(curso, novos_dados):
        return BaseDados.atualizarCurso(curso, novos_dados)
    
    @staticmethod
    def deletarCurso(curso):
        return BaseDados.deletarCurso(curso)
    
    @staticmethod
    def cadastrarDisciplina(disciplina):
        return BaseDados.cadastrarDisciplina(disciplina)
    
    @staticmethod
    def buscarDisciplina(disciplina):
        return BaseDados.buscarDisciplina(disciplina)
    
    @staticmethod
    def atualizarDisciplina(disciplina, novos_dados):
        return BaseDados.atualizarDisciplina(disciplina, novos_dados)
    
    @staticmethod
    def deletarDisciplina(disciplina):
        return BaseDados.deletarDisciplina(disciplina)
    
    @staticmethod
    def cadastrarSala(sala):
        return BaseDados.cadastrarSala(sala)
    
    @staticmethod
    def buscarSala(sala):
        return BaseDados.buscarSala(sala)
    
    @staticmethod
    def atualizarSala(sala, novos_dados):
        return BaseDados.atualizarSala(sala, novos_dados)
    
    @staticmethod
    def deletarSala(sala):
        return BaseDados.deletarSala(sala)
    
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
        
    @staticmethod
    def deletarBase():
        BaseDados.deletarBase()