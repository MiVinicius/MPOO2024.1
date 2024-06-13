import sys
sys.path.append('.')
from ProjetoCadastro.Model.BaseDadosModel import BaseDadosModel
class BaseDadosController:
    
    @staticmethod
    def inicializarBase():
        BaseDadosModel._inicializarBase()
        
    @staticmethod
    def cadastrarAluno(aluno):
        return BaseDadosModel.cadastrarAluno(aluno)
        
    @staticmethod
    def buscarAluno(aluno):
        return BaseDadosModel.buscarAluno(aluno)
    
    @staticmethod
    def atualizarAluno(aluno, novos_dados):
        return BaseDadosModel.atualizarAluno(aluno, novos_dados)
    
    @staticmethod
    def deletarAluno(aluno):
        return BaseDadosModel.deletarAluno(aluno)
    
    @staticmethod
    def cadastrarServidor(servidor):
        return BaseDadosModel.cadastrarServidor(servidor)
    
    @staticmethod
    def buscarServidor(servidor):
        return BaseDadosModel.buscarServidor(servidor)
    
    @staticmethod
    def atualizarServidor(servidor, novos_dados):
        return BaseDadosModel.atualizarServidor(servidor, novos_dados)
    
    @staticmethod
    def deletarServidor(servidor):
        return BaseDadosModel.deletarServidor(servidor)
    
    @staticmethod
    def cadastrarProfessor(professor):
        return BaseDadosModel.cadastrarProfessor(professor)
    
    @staticmethod
    def buscarProfessor(professor):
        return BaseDadosModel.buscarProfessor(professor)
    
    @staticmethod
    def atualizarProfessor(professor, novos_dados):
        return BaseDadosModel.atualizarProfessor(professor, novos_dados)
    
    @staticmethod
    def deletarProfessor(professor):
        return BaseDadosModel.deletarProfessor(professor)
    
    @staticmethod
    def cadastrarCoordenador(coordenador):
        return BaseDadosModel.cadastrarCoordenador(coordenador)
    
    @staticmethod
    def buscarCoordenador(coordenador):
        return BaseDadosModel.buscarCoordenador(coordenador)
    
    @staticmethod
    def atualizarCoordenador(coordenador, novos_dados):
        return BaseDadosModel.atualizarCoordenador(coordenador, novos_dados)
    
    @staticmethod
    def deletarCoordenador(coordenador):
        return BaseDadosModel.deletarCoordenador(coordenador)
    
    @staticmethod
    def cadastrarDiretor(diretor):
        return BaseDadosModel.cadastrarDiretor(diretor)
    
    @staticmethod
    def buscarDiretor(diretor):
        return BaseDadosModel.buscarDiretor(diretor)
    
    @staticmethod
    def atualizarDiretor(diretor, novos_dados):
        return BaseDadosModel.atualizarDiretor(diretor, novos_dados)
    
    @staticmethod
    def deletarDiretor(diretor):
        return BaseDadosModel.deletarDiretor(diretor)
    
    @staticmethod
    def cadastrarCurso(curso):
        return BaseDadosModel.cadastrarCurso(curso)
    
    @staticmethod
    def buscarCurso(curso):
        return BaseDadosModel.buscarCurso(curso)
    
    @staticmethod
    def atualizarCurso(curso, novos_dados):
        return BaseDadosModel.atualizarCurso(curso, novos_dados)
    
    @staticmethod
    def deletarCurso(curso):
        return BaseDadosModel.deletarCurso(curso)
    
    @staticmethod
    def cadastrarDisciplina(disciplina):
        return BaseDadosModel.cadastrarDisciplina(disciplina)
    
    @staticmethod
    def buscarDisciplina(disciplina):
        return BaseDadosModel.buscarDisciplina(disciplina)
    
    @staticmethod
    def atualizarDisciplina(disciplina, novos_dados):
        return BaseDadosModel.atualizarDisciplina(disciplina, novos_dados)
    
    @staticmethod
    def deletarDisciplina(disciplina):
        return BaseDadosModel.deletarDisciplina(disciplina)
    
    @staticmethod
    def cadastrarSala(sala):
        return BaseDadosModel.cadastrarSala(sala)
    
    @staticmethod
    def buscarSala(sala):
        return BaseDadosModel.buscarSala(sala)
    
    @staticmethod
    def atualizarSala(sala, novos_dados):
        return BaseDadosModel.atualizarSala(sala, novos_dados)
    
    @staticmethod
    def deletarSala(sala):
        return BaseDadosModel.deletarSala(sala)
    
    @staticmethod
    def listarAlunos():
        BaseDadosModel.listarAlunos()
        
    @staticmethod
    def listarServidores():
        BaseDadosModel._listarServidores()
        
    @staticmethod
    def listarProfessores():
        BaseDadosModel.listarProfessores()
        
    @staticmethod
    def listarCoordenadores():
        BaseDadosModel.listarCoordenadores()
        
    @staticmethod
    def listarDiretores():
        BaseDadosModel.listarDiretores()
        
    @staticmethod
    def listarCursos():
        BaseDadosModel.listarCursos()
        
    @staticmethod
    def listarDisciplinas():
        BaseDadosModel.listarDisciplinas()
        
    @staticmethod
    def listarSalas():
        BaseDadosModel.listarSalas()
        
    @staticmethod
    def deletarBase():
        BaseDadosModel.deletarBase()