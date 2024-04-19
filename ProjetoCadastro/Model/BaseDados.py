
from Aluno import Aluno
# from Professor import Professor
# from Coordenador import Coordenador
# from Diretor import Diretor
# from Servidor import Servidor
class BaseDados():
    
    alunos = []
    servidores = []
    cursos = []
    disciplinas = []
    salas = []
    
    
    def inicializarBase(self):
        aluno = Aluno("Misael")
        self.cadastrarPessoa(aluno)
        # professor = Professor("Julian", "124.735.846-72")
        # self.cadastrarPessoa(professor)
        # coordenador = Coordenador("Gean", "034.346.786-74", "Basquete")
        # self.cadastrarPessoa(coordenador)
        # diretor = Diretor("Kauan", "405.695.954-60", "UARRISLO")
        # self.cadastrarPessoa(diretor)
    
    
    def cadastrarAluno(self):
        aluno = Aluno(str(input("Digite o nome do aluno: \n")))
        self.cadastrarPessoa(aluno)
    
    def cadastrarServidor(self):
        pass
    
    def cadastrarProfessor(self):
        pass
    
    def cadastrarCoordenador(self):
        pass
    
    def cadastrarDiretor(self):
        pass
    
    
    
    def cadastrarPessoa(self, pessoa):
        if isinstance(pessoa, Aluno):
            if pessoa not in BaseDados.alunos:
                BaseDados.alunos.append(pessoa)
            else:
                return False
        # if isinstance(pessoa, Servidor):
        #     if pessoa not in BaseDados.servidores:
        #         BaseDados.servidores.append(pessoa)
        #     else:
        #         return False
        # if isinstance(pessoa, Professor):
        #     if pessoa not in BaseDados.servidores:
        #         BaseDados.servidores.append(pessoa)
        #     else:
        #         return False
        # if isinstance(pessoa, Coordenador):
        #     if pessoa not in BaseDados.servidores:
        #         BaseDados.servidores.append(pessoa)
        #     else:
        #         return False
        # if isinstance(pessoa, Diretor):
        #     if pessoa not in BaseDados.servidores:
        #         BaseDados.servidores.append(pessoa)
        #     else:
        #         return False
    
    
    
    def cadastrarCurso(self, curso):
        pass
    
    def cadastrarDisciplina(self, disciplina):
        pass
    
    def cadastrarEndereco(self, endereco):
        pass
    
    def cadastrarSala(self, sala):
        pass
    
    def atualizarPessoa(self, id_pessoa, novos_dados):
        pass
    
    def buscarPessoa(self, id_pessoa):
        pass
    
    def deletarPessoa(self, id_pessoa):
        pass
    
    def atualizarCurso(self, id_curso, novos_dados):
        pass
    
    def buscarCurso(self, id_curso):
        pass
    
    def deletarCurso(self, id_curso):
        pass