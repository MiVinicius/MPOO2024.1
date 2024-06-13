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
class BaseDadosModel():
    
    alunos :list = []    
    servidores :list = []
    cursos :list = []
    disciplinas :list = []
    salas :list = []
    
    @staticmethod
    def _inicializarBase() -> None:
        aluno = Aluno("Misael", "999.999.999-99")
        BaseDadosModel.cadastrarAluno(aluno)
        aluno = Aluno("Elias", "426.272.465.04")
        BaseDadosModel.cadastrarAluno(aluno)
        servidor = Servidor("Jurisclebson", "400.289.228-00")
        BaseDadosModel.cadastrarServidor(servidor)
        professor = Professor("Juliano", "124.735.846-73")
        BaseDadosModel.cadastrarProfessor(professor)
        coordenador = Coordenador("Gean", "034.346.786-74")
        BaseDadosModel.cadastrarCoordenador(coordenador)
        diretor = Diretor("Mauro", "405.695.954-60")
        BaseDadosModel.cadastrarDiretor(diretor)

    @staticmethod
    def cadastrarAluno(Aluno):
        BaseDadosModel.alunos.append(Aluno)
        return True
    
    @staticmethod
    def cadastrarServidor(Servidor):
        BaseDadosModel.servidores.append(Servidor)
        return True
    
    @staticmethod
    def cadastrarProfessor(Professor):
        BaseDadosModel.servidores.append(Professor)
        return True
    
    @staticmethod
    def cadastrarCoordenador(Coordenador):
        BaseDadosModel.servidores.append(Coordenador)
        return True
    
    @staticmethod
    def cadastrarDiretor(Diretor):
        BaseDadosModel.servidores.append(Diretor)
        return True
    
    @staticmethod
    def cadastrarCurso(Curso):
        BaseDadosModel.cursos.append(Curso)
        return True
    
    @staticmethod
    def cadastrarDisciplina(Disciplina):
        BaseDadosModel.disciplinas.append(Disciplina)
        return True
    
    @staticmethod
    def cadastrarSala(Sala):
        BaseDadosModel.salas.append(Sala)
        return True
    
    @staticmethod
    def buscarAluno(aluno):
        for aluno_atual in BaseDadosModel.alunos:
            if aluno_atual._getNome() == aluno._getNome():
                if aluno_atual._getCpf() == aluno._getCpf():
                    return aluno_atual
        return None
    
    @staticmethod
    def buscarServidor(servidor: Servidor):
        for servidor_atual in BaseDadosModel.servidores:
            if isinstance(servidor_atual, Servidor):
                if  servidor_atual._getNome()==servidor._getNome():
                    if servidor_atual._getCpf() == servidor._getCpf():
                        return servidor_atual
        return None
    
    @staticmethod
    def buscarProfessor(professor):
        for professor_atual in BaseDadosModel.servidores:
            if isinstance(professor_atual, Professor):
                if professor_atual._getNome() == professor._getNome():
                    if professor_atual._getCpf() == professor._getCpf():
                        return professor_atual
        return None
    
    @staticmethod
    def buscarCoordenador(coordenador):
        for coordenador_atual in BaseDadosModel.servidores:
            if isinstance(coordenador_atual, Coordenador):
                if coordenador_atual._getNome() == coordenador._getNome():
                    if coordenador_atual._getCpf() == coordenador._getCpf():
                        return coordenador_atual
        return None
    
    @staticmethod
    def buscarDiretor(diretor):
        for diretor_atual in BaseDadosModel.servidores:
            if isinstance(diretor_atual, Diretor):
                if diretor_atual._getNome() == diretor._getNome():
                    if diretor_atual._getCpf() == diretor._getCpf():
                        return diretor_atual
        return None

    @staticmethod
    def buscarCurso(id_curso):
        for curso in BaseDadosModel.cursos:
            if curso._getNome() == id_curso._getNome():
                if curso._getPeriodo() == id_curso._getPeriodo():
                    return curso
        return None
    
    @staticmethod
    def buscarDisciplina(id_disciplina):
        for disciplina in BaseDadosModel.disciplinas:
            if disciplina._getNome() == id_disciplina._getNome():
                return disciplina
        return None
    
    @staticmethod
    def buscarSala(id_sala):
        for sala in BaseDadosModel.salas:
            if sala._getNome() == id_sala._getNome():
                if sala._getBloco() == id_sala._getBloco():
                    return sala
        return None
    
    @staticmethod
    def atualizarAluno(id_aluno, novos_dados):
        for aluno in BaseDadosModel.alunos:
            if aluno._getNome() == id_aluno._getNome():
                if aluno._getCpf() == id_aluno._getCpf():
                    BaseDadosModel.alunos.index(aluno)._setNome(novos_dados._getNome())
                    BaseDadosModel.alunos.index(aluno)._setCpf(novos_dados._getCpf())
                    BaseDadosModel.alunos.index(aluno)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarServidor(id_pessoa, novos_dados):
        for servidor in BaseDadosModel.servidores:
            if servidor._getNome() == id_pessoa._getNome():
                if servidor._getCpf() == id_pessoa._getCpf():
                    BaseDadosModel.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDadosModel.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDadosModel.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarProfessor(professor, novos_dados):
        for servidor in BaseDadosModel.servidores:
            if servidor._getNome() == professor._getNome():
                if servidor._getCpf() == professor._getCpf():
                    BaseDadosModel.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDadosModel.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDadosModel.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarCoordenador(Coordenador, novos_dados):
        for servidor in BaseDadosModel.servidores:
            if servidor._getNome() == Coordenador._getNome():
                if servidor._getCpf() == Coordenador._getCpf():
                    BaseDadosModel.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDadosModel.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDadosModel.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarDiretor(Diretor, novos_dados):
        for servidor in BaseDadosModel.servidores:
            if servidor._getNome() == Diretor._getNome():
                if servidor._getCpf() == Diretor._getCpf():
                    BaseDadosModel.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDadosModel.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDadosModel.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    @staticmethod
    def atualizarCurso(id_curso, novos_dados):
        for curso in BaseDadosModel.cursos:
            if curso._getNome() == id_curso._getNome():
                BaseDadosModel.cursos.index(curso)._setNome(novos_dados._getNome()) 
                BaseDadosModel.cursos.index(curso)._setPeriodo(novos_dados._getPeriodo())
                BaseDadosModel.cursos.index(curso)._setCoordenador(novos_dados._getCoordenador())
                return True
        return False
    
    @staticmethod
    def atualizarDisciplina(id_disciplina, novos_dados): 
        for disciplina in BaseDadosModel.disciplinas:
            if disciplina._getNome() == id_disciplina._getNome():
                BaseDadosModel.disciplinas.index(disciplina)._setNome(novos_dados._getNome())
                return True
        return False
    
    @staticmethod
    def atualizarSala(id_sala, novos_dados):
        for sala in BaseDadosModel.salas:
            if sala._getSalaNumero() == id_sala._getSalaNumero() and sala._getBlocoNumero() == id_sala._getBlocoNumero():
                BaseDadosModel.salas.index(sala)._setNome(novos_dados._getNome()), BaseDadosModel.salas.index(sala)._setBloco(novos_dados._getBloco())
                return True
        return False
    
    @staticmethod
    def deletarAluno(Aluno):
        BaseDadosModel.alunos.remove(Aluno)
        return True
    
    @staticmethod
    def deletarServidor(Servidor):
        BaseDadosModel.servidores.remove(Servidor)
        return True
    
    @staticmethod
    def deletarProfessor(Professor):
        BaseDadosModel.servidores.remove(Professor)
        return True
    
    @staticmethod
    def deletarCoordenador(Coordenador):
        BaseDadosModel.servidores.remove(Coordenador)
        return True
    
    @staticmethod
    def deletarDiretor(Diretor):
        BaseDadosModel.servidores.remove(Diretor)
        return True
    
    @staticmethod
    def deletarCurso(Curso):
        Curso._setDisciplinas(None) 
        BaseDadosModel.cursos.remove(Curso)  
        return True
    
    @staticmethod
    def deletarDisciplina(Disciplina):
        BaseDadosModel.disciplinas.remove(Disciplina)
        return True
    
    @staticmethod
    def deletarSala(Sala):
        return BaseDadosModel.salas.remove(Sala)
    
    @staticmethod
    def deletarBase():      
        BaseDadosModel.alunos.clear()
        BaseDadosModel.servidores.clear()
        print("Base Deletada com Sucesso!")
    
    @staticmethod
    def listarAlunos():
        print("Lista dos alunos:")
        for aluno in BaseDadosModel.alunos:
            if isinstance(aluno, Aluno):
                print(aluno._getNome(), aluno._getCpf(), aluno._getMatricula(), aluno._getEndereco(), aluno._getCurso(), aluno._getDisciplina()) 
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def _listarServidores():
        print("Lista dos servidores:")
        for servidor in BaseDadosModel.servidores:
            if isinstance(servidor, Servidor) and not isinstance(servidor, Professor) and not isinstance(servidor, Coordenador)and not isinstance(servidor, Diretor):
                print(servidor._getNome(), servidor._getCpf(), servidor._getEndereco())
        print(input("Aperte Enter para continuar"))
        
    @staticmethod
    def listarProfessores():
        print("Lista dos professores:")
        for professor in BaseDadosModel.servidores:
            if isinstance(professor, Professor) and not isinstance(professor, Coordenador) and not isinstance(professor, Diretor):
                print(professor._getNome(), professor._getCpf(), professor._getEndereco(), professor._getDisciplinas())
        print(input("Aperte Enter para continuar"))
        
    @staticmethod
    def listarCoordenadores():
        print("Lista dos coordenadores:")
        for coordenador in BaseDadosModel.servidores:
            if isinstance(coordenador, Coordenador) and not isinstance(coordenador, Diretor):
                print(coordenador._getNome(), coordenador._getCpf(), coordenador._getEndereco())
        print(input("Aperte Enter para continuar"))
        
    @staticmethod
    def listarDiretores():
        print("Lista dos diretores:")
        for diretor in BaseDadosModel.servidores:
            if isinstance(diretor, Diretor):
                print(diretor._getNome(), diretor._getCpf(), diretor._getEndereco())
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def listarCursos():
        print("Lista dos Cursos:")
        for curso in BaseDadosModel.cursos:
            if isinstance(curso, Curso):
                print(curso._getNome(), curso._getPeriodo())
                print(curso._getDisciplinas())
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def listarDisciplinas():
        print("Lista das Disciplinas:")
        for disciplina in BaseDadosModel.disciplinas:
            if isinstance(disciplina, Disciplina):
                print(disciplina._getNome(), disciplina._getSala())
        print(input("Aperte Enter para continuar"))
    
    @staticmethod
    def listarSalas():
        print("Lista das Salas:")
        for sala in BaseDadosModel.salas:
            if isinstance(sala, Sala):
                print(sala._getSalaNumero(), sala._getBlocoNumero())
        print(input("Aperte Enter para continuar"))
    
    
    
if __name__ != "__main__":
    BaseDadosModel._inicializarBase()             # por algum motivo, isso precisou ser feito dentro da classe