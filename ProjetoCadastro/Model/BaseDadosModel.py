import sys
sys.path.append('.')
from ProjetoCadastro.Model.AlunoModel import Aluno
from ProjetoCadastro.Model.ServidorModel import Servidor
from ProjetoCadastro.Model.ProfessorModel import Professor
from ProjetoCadastro.Model.CoordenadorModel import Coordenador
from ProjetoCadastro.Model.DiretorModel import Diretor
from ProjetoCadastro.Model.CursoModel import Curso
from ProjetoCadastro.Model.DisciplinaModel import Disciplina
from ProjetoCadastro.Model.SalaModel import Sala

# Create
class BaseDados():
    
    alunos :list = []    
    servidores :list = []
    cursos :list = []
    disciplinas :list = []
    salas :list = []
    
    @staticmethod
    def _inicializarBase() -> None:
        aluno = Aluno("Misael", "999.999.999-99")
        BaseDados.cadastrarAluno(aluno)
        aluno = Aluno("Elias", "426.272.465.04")
        BaseDados.cadastrarAluno(aluno)
        professor = Professor("Juliano", "124.735.846-73")
        BaseDados.cadastrarProfessor(professor)
        coordenador = Coordenador("Gean", "034.346.786-74")
        BaseDados.cadastrarCoordenador(coordenador)
        diretor = Diretor("Mauro", "405.695.954-60")
        BaseDados.cadastrarDiretor(diretor)

    @staticmethod
    def cadastrarAluno(Aluno):
        BaseDados.alunos.append(Aluno)
        return True
    
    @staticmethod
    def cadastrarServidor(Servidor):
        BaseDados.servidores.append(Servidor)
        return True
    
    @staticmethod
    def cadastrarProfessor(Professor):
        BaseDados.servidores.append(Professor)
        return True
    
    @staticmethod
    def cadastrarCoordenador(Coordenador):
        BaseDados.servidores.append(Coordenador)
        return True
    
    @staticmethod
    def cadastrarDiretor(Diretor):
        BaseDados.servidores.append(Diretor)
        return True
    
    @staticmethod
    def cadastrarCurso(Curso):
        BaseDados.cursos.append(Curso)
        return True
    
    @staticmethod
    def cadastrarDisciplina(Disciplina):
        BaseDados.disciplinas.append(Disciplina)
        return True
    
    @staticmethod
    def cadastrarSala(Sala):
        BaseDados.salas.append(Sala)
        return True
    
    @staticmethod
    def buscarAluno(Aluno):
        for aluno_atual in BaseDados.alunos:
            if aluno_atual._getNome() == Aluno._getNome():
                if aluno_atual._getCpf() == Aluno._getCpf():
                    return aluno_atual
        return None
    
    @staticmethod
    def buscarServidor(Servidor):
        for servidor_atual in BaseDados.servidores:
            if isinstance(Servidor, Servidor):
                if  servidor_atual._getNome()==Servidor._getNome():
                    if servidor_atual._getCpf() == Servidor._getCpf():
                        return servidor_atual
        return None
    
    @staticmethod
    def buscarProfessor(Professor):
        for professor in BaseDados.servidores:
            if isinstance(Professor, Professor):
                if professor._getNome() == Professor._getNome():
                    if professor._getCpf() == Professor._getCpf():
                        return professor
        return None
    
    @staticmethod
    def buscarCoordenador(Coordenador):
        for coordenador in BaseDados.servidores:
            if isinstance(Coordenador, Coordenador):
                if coordenador._getNome() == Coordenador._getNome():
                    if coordenador._getCpf() == Coordenador._getCpf():
                        return coordenador
        return None
    
    @staticmethod
    def buscarDiretor(Diretor):
        for diretor in BaseDados.servidores:
            if isinstance(Diretor, Diretor):
                if diretor._getNome() == Diretor._getNome():
                    if diretor._getCpf() == Diretor._getCpf():
                        return diretor
        return None

    @staticmethod
    def buscarCurso(id_curso):
        for curso in BaseDados.cursos:
            if curso._getNome() == id_curso._getNome():
                if curso._getPeriodo() == id_curso._getPeriodo():
                    return curso
        return None
    
    @staticmethod
    def buscarDisciplina(id_disciplina):
        for disciplina in BaseDados.disciplinas:
            if disciplina._getNome() == id_disciplina._getNome():
                return disciplina
        return None
    
    @staticmethod
    def buscarSala(id_sala):
        for sala in BaseDados.salas:
            if sala._getNome() == id_sala._getNome():
                if sala._getBloco() == id_sala._getBloco():
                    return sala
        return None
    
    @staticmethod
    def atualizarAluno(id_aluno, novos_dados):
        for aluno in BaseDados.alunos:
            if aluno._getNome() == id_aluno._getNome():
                if aluno._getCpf() == id_aluno._getCpf():
                    BaseDados.alunos.index(aluno)._setNome(novos_dados._getNome())
                    BaseDados.alunos.index(aluno)._setCpf(novos_dados._getCpf())
                    BaseDados.alunos.index(aluno)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarServidor(id_pessoa, novos_dados):
        for servidor in BaseDados.servidores:
            if servidor._getNome() == id_pessoa._getNome():
                if servidor._getCpf() == id_pessoa._getCpf():
                    BaseDados.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDados.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDados.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarProfessor(professor, novos_dados):
        for servidor in BaseDados.servidores:
            if servidor._getNome() == professor._getNome():
                if servidor._getCpf() == professor._getCpf():
                    BaseDados.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDados.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDados.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarCoordenador(Coordenador, novos_dados):
        for servidor in BaseDados.servidores:
            if servidor._getNome() == Coordenador._getNome():
                if servidor._getCpf() == Coordenador._getCpf():
                    BaseDados.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDados.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDados.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarDiretor(Diretor, novos_dados):
        for servidor in BaseDados.servidores:
            if servidor._getNome() == Diretor._getNome():
                if servidor._getCpf() == Diretor._getCpf():
                    BaseDados.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDados.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDados.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarCurso(id_curso, novos_dados):
        for curso in BaseDados.cursos:
            if curso._getNome() == id_curso._getNome():
                BaseDados.cursos.index(curso)._setNome(novos_dados._getNome()) 
                BaseDados.cursos.index(curso)._setPeriodo(novos_dados._getPeriodo())
                BaseDados.cursos.index(curso)._setCoordenador(novos_dados._getCoordenador())
                return True
        return False
    
    @staticmethod
    def atualizarDisciplina(id_disciplina, novos_dados): 
        for disciplina in BaseDados.disciplinas:
            if disciplina._getNome() == id_disciplina._getNome():
                BaseDados.disciplinas.index(disciplina)._setNome(novos_dados._getNome())
                return True
        return False
    
    @staticmethod
    def atualizarSala(id_sala, novos_dados):
        for sala in BaseDados.salas:
            if sala._getSalaNumero() == id_sala._getSalaNumero() and sala._getBlocoNumero() == id_sala._getBlocoNumero():
                BaseDados.salas.index(sala)._setNome(novos_dados._getNome()), BaseDados.salas.index(sala)._setBloco(novos_dados._getBloco())
                return True
        return False
    
    @staticmethod
    def deletarAluno(Aluno):
        BaseDados.alunos.remove(Aluno)
        return True
    
    @staticmethod
    def deletarServidor(Servidor):
        BaseDados.servidores.remove(Servidor)
        return True
    
    @staticmethod
    def deletarProfessor(Professor):
        BaseDados.servidores.remove(Professor)
        return True
    
    @staticmethod
    def deletarCoordenador(Coordenador):
        BaseDados.servidores.remove(Coordenador)
        return True
    
    @staticmethod
    def deletarDiretor(Diretor):
        BaseDados.servidores.remove(Diretor)
        return True
    
    @staticmethod
    def deletarCurso(Curso):
        Curso._setDisciplinas(None) 
        BaseDados.cursos.remove(Curso)  
        return True
    
    @staticmethod
    def deletarDisciplina(Disciplina):
        BaseDados.disciplinas.remove(Disciplina)
        return True
    
    @staticmethod
    def deletarSala(Sala):
        return BaseDados.salas.remove(Sala)
    
    @staticmethod
    def deletarBase():      
        BaseDados.alunos.clear()
        BaseDados.servidores.clear()
        print("Base Deletada com Sucesso!")
    
    @staticmethod
    def listarAlunos():
        print("Lista dos alunos:")
        for aluno in BaseDados.alunos:
            if isinstance(aluno, Aluno):
                print(aluno._getNome(), aluno._getCpf(), aluno._getMatricula(), aluno._getEndereco(), aluno._getCurso(), aluno._getDisciplina()) 
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def listarServidores():
        print("Lista dos servidores:")
        for servidor in BaseDados.servidores:
            if isinstance(servidor, Servidor):
                print(servidor._getNome(), servidor._getCpf(), servidor._getEndereco())
        print(input("Aperte Enter para continuar"))
        
    @staticmethod
    def listarProfessores():
        print("Lista dos professores:")
        for professor in BaseDados.servidores:
            if isinstance(professor, Professor):
                print(professor._getNome(), professor._getCpf(), professor._getEndereco(), professor._getDisciplinas())
        print(input("Aperte Enter para continuar"))
        
    @staticmethod
    def listarCoordenadores():
        print("Lista dos coordenadores:")
        for coordenador in BaseDados.servidores:
            if isinstance(coordenador, Coordenador):
                print(coordenador._getNome(), coordenador._getCpf(), coordenador._getEndereco())
        print(input("Aperte Enter para continuar"))
        
    @staticmethod
    def listarDiretores():
        print("Lista dos diretores:")
        for diretor in BaseDados.servidores:
            if isinstance(diretor, Diretor):
                print(diretor._getNome(), diretor._getCpf(), diretor._getEndereco())
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def listarCursos():
        print("Lista dos Cursos:")
        for curso in BaseDados.cursos:
            if isinstance(curso, Curso):
                print(curso._getNome(), curso._getPeriodo())
                print(curso._getDisciplinas())
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def listarDisciplinas():
        print("Lista das Disciplinas:")
        for disciplina in BaseDados.disciplinas:
            if isinstance(disciplina, Disciplina):
                print(disciplina._getNome(), disciplina._getSala())
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def listarSalas():
        print("Lista das Salas:")
        for sala in BaseDados.salas:
            if isinstance(sala, Sala):
                print(sala._getSalaNumero(), sala._getBlocoNumero())
        print(input("Aperte Enter para continuar"))
    
    
    
if __name__ != "__main__":
    BaseDados._inicializarBase()             # por algum motivo, isso precisou ser feito dentro da classe