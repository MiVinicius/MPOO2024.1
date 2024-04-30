import sys
sys.path.append('.')
from ProjetoCadastro.Model.Aluno import Aluno
from ProjetoCadastro.Model.Servidor import Servidor
from ProjetoCadastro.Model.Professor import Professor
from ProjetoCadastro.Model.Coordenador import Coordenador
from ProjetoCadastro.Model.Diretor import Diretor
from ProjetoCadastro.Model.Curso import Curso
from ProjetoCadastro.Model.Disciplina import Disciplina
from ProjetoCadastro.Model.Sala import Sala

# Create
class BaseDados():
    
    alunos :list = []    # no dia que isso tiver que ficar privado, esse código já era
    servidores :list = []
    cursos :list = []
    disciplinas :list = []
    salas :list = []
    
    @staticmethod
    def inicializarBase() -> None:
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
    def cadastrarAluno(aluno):
        BaseDados.alunos.append(aluno)
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
    
    def cadastrarCurso(self, Curso):
        BaseDados.cursos.append(Curso)
        return True
    
    def cadastrarDisciplina(self, Disciplina):
        BaseDados.disciplinas.append(Disciplina)
        return True
    
    def cadastrarSala(self, Sala):
        BaseDados.salas.append(Sala)
        return True
    
    @staticmethod
    def buscarAluno(aluno):
        for aluno_atual in BaseDados.alunos:
            if aluno_atual._getNome() == aluno._getNome():
                if aluno_atual._getCpf() == aluno._getCpf():
                    return aluno_atual
        return None
    
    def buscarServidor(self, servidor_procurado):
        for servidor_atual in BaseDados.servidores:
            if  servidor_atual._getNome()==servidor_procurado._getNome():
                if servidor_atual._getCpf() == servidor_procurado._getCpf():
                    return servidor_atual
        return None

    def buscarCurso(self, id_curso):
        for curso in BaseDados.cursos:
            if curso._getNome() == id_curso._getNome():
                return curso
    
    def buscarDisciplina(self, id_disciplina):
        for disciplina in BaseDados.disciplinas:
            if disciplina._getNome() == id_disciplina:
                return disciplina
    
    def buscarSala(self, id_sala):
        for sala in BaseDados.salas:
            if sala._getNome() == id_sala._getNome():
                if sala._getBloco() == id_sala._getBloco():
                    return sala
        return None
    
    def atualizarAluno(self, id_aluno, novos_dados):
        for aluno in BaseDados.alunos:
            if aluno._getNome() == id_aluno._getNome():
                if aluno._getCpf() == id_aluno._getCpf():
                    BaseDados.alunos.index(aluno)._setNome(novos_dados._getNome())
                    BaseDados.alunos.index(aluno)._setCpf(novos_dados._getCpf())
                    BaseDados.alunos.index(aluno)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    def atualizarServidor(self, id_pessoa, novos_dados):
        for servidor in BaseDados.servidores:
            if servidor._getNome() == id_pessoa._getNome():
                if servidor._getCpf() == id_pessoa._getCpf():
                    BaseDados.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDados.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDados.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    def atualizarCurso(self, id_curso, novos_dados):
        for curso in BaseDados.cursos:
            if curso._getNome() == id_curso._getNome():
                BaseDados.cursos.index(curso)._setNome(novos_dados._getNome()) 
                BaseDados.cursos.index(curso)._setPeriodo(novos_dados._getPeriodo())
                BaseDados.cursos.index(curso)._setCoordenador(novos_dados._getCoordenador())
                return True
        return False
    
    def atualizarDisciplina(self, id_disciplina, novos_dados): 
        for disciplina in BaseDados.disciplinas:
            if disciplina._getNome() == id_disciplina._getNome():
                BaseDados.disciplinas.index(disciplina)._setNome(novos_dados._getNome())
                return True
        return False
    
    def atualizarSala(self, id_sala, novos_dados):
        for sala in BaseDados.salas:
            if sala._getSalaNumero() == id_sala._getSalaNumero() and sala._getBlocoNumero() == id_sala._getBlocoNumero():
                BaseDados.salas.index(sala)._setNome(novos_dados._getNome()), BaseDados.salas.index(sala)._setBloco(novos_dados._getBloco())
                return True
        return False
    
    def deletarAluno(self, Aluno):
        BaseDados.alunos.remove(Aluno)
        return True
    
    def deletarServidor(self, Servidor):
        BaseDados.servidores.remove(Servidor)
        return True
    
    def deletarCurso(self, Curso):
        Curso._setDisciplinas(None) 
        BaseDados.cursos.remove(Curso)  
        return True
    
    def deletarDisciplina(self, Disciplina):
        BaseDados.disciplinas.remove(Disciplina)
        return True
    
    def deletarSala(self, Sala):
        return BaseDados.salas.remove(Sala)
    
    def deletarBase(self):      
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
    BaseDados.inicializarBase()             # por algum motivo, isso precisou ser feito dentro da classe