
from Aluno import Aluno
from Professor import Professor
from Coordenador import Coordenador
from Diretor import Diretor
from Servidor import Servidor
from Endereco import Endereco
from Disciplina import Disciplina
from Sala import Sala
from Curso import Curso


class BaseDados():
    
    alunos :list = []
    servidores :list = []
    cursos :list = []
    disciplinas :list = []
    salas :list = []
    
    def inicializarBase(self):
        aluno = Aluno("Misael", "999")
        self.cadastrarPessoa(aluno)
        professor = Professor("Julian", "124.735.846-72")
        self.cadastrarPessoa(professor)
        coordenador = Coordenador("Gean", "034.346.786-74")
        self.cadastrarPessoa(coordenador)
        diretor = Diretor("Kauan", "405.695.954-60")
        self.cadastrarPessoa(diretor)
    
    def cadastrarAluno(self):
        try:  # ta certo isso?
            aluno = Aluno((str(input("Digite o nome do Aluno: \n"))), int(input("Digite o Cpf: \n")))
            self.cadastrarPessoa(aluno)
        except TypeError:
            print("Erro de tipo de input de dado!")
            self.cadastrarAluno()
        except ValueError:
            print("erro de valor do input de dado")
            self.cadastrarAluno()
        finally:
            print("agora deu ruim mesmo!")
            self.cadastrarAluno() # não tem pra onde correr
    
    def cadastrarServidor(self):
        servidor = Servidor((str(input("Digite o nome do Servidor: \n"))), str(input("Digite o cpf: \n")))
        self.cadastrarServidor(servidor)
    
    def cadastrarProfessor(self):
        professor = Professor(str(input("Digite o nome do Professor: \n")), str(input("Digite o cpf: \n")))
        self.cadastrarProfessor(professor)
        
    def cadastrarCoordenador(self):
        coordenador = Coordenador(str(input("Digite o nome do Coordenador: \n")), str(input("Digite o cpf: \n")))
        self.cadastrarCoordenador(coordenador)
    
    def cadastrarDiretor(self):
        diretor = Diretor(str(input("Digite o nome do Diretor: \n")), str(input("Digite o cpf: \n")))
        self.cadastrarDiretor(diretor)
    
    def cadastrarPessoa(self, pessoa: object):  # deve ter alguma forma de reduzir isso aqui...
        if isinstance(pessoa, Aluno):
            if pessoa not in BaseDados.alunos:
                BaseDados.alunos.append(pessoa)
            else:
                return False
        if isinstance(pessoa, Servidor):
            if pessoa not in BaseDados.servidores:
                BaseDados.servidores.append(pessoa)
            else:
                return False
        if isinstance(pessoa, Professor):
            if pessoa not in BaseDados.servidores:
                BaseDados.servidores.append(pessoa)
            else:
                return False
        if isinstance(pessoa, Coordenador):
            if pessoa not in BaseDados.servidores:
                BaseDados.servidores.append(pessoa)
            else:
                return False
        if isinstance(pessoa, Diretor):
            if pessoa not in BaseDados.servidores:
                BaseDados.servidores.append(pessoa)
            else:
                return False
    
    def cadastrarCurso(self):
        curso = Curso(str(input("Digite o nome do curso: \n")),
                    str(input("Digite o período do curso: \n")))
        BaseDados.cursos.append(curso)
        return self
    
    def passarCurso(self, Curso, pessoa):
        if isinstance(pessoa, Aluno):
            pessoa._setCurso(Curso)
        if isinstance(pessoa, Servidor):
            pessoa._setCurso(Curso)
        if isinstance(pessoa, Professor):
            pessoa._setCurso(Curso)
        if isinstance(pessoa, Coordenador):
            pessoa._setCurso(Curso)
        if isinstance(pessoa, Diretor):
            pessoa._setCurso(Curso)
        return True
        
    def cadastrarDisciplina(self):
        disciplina = Disciplina(str(input("Digite o nome da disciplina: \n")), self.cadastrarSala())
        BaseDados.disciplinas.append(disciplina)
        return disciplina
    
    def passarDisciplina(self, Disciplina, pessoa):
        if isinstance(pessoa, Aluno):
            pessoa._setDisciplina(Disciplina)
        if isinstance(pessoa, Servidor):
            pessoa._setDisciplina(Disciplina)
        if isinstance(pessoa, Professor):
            pessoa._setDisciplina(Disciplina)
        if isinstance(pessoa, Coordenador):
            pessoa._setDisciplina(Disciplina)
        if isinstance(pessoa, Diretor):
            pessoa._setDisciplina(Disciplina)
        return True
    
    def cadastrarSala(self):
        sala = Sala(str(input("Digite o numero da sala: \n")), 
                    str(input("Digite o bloco da sala: \n")))
        BaseDados.salas.append(sala)
        return self
    
    def passarSala(self, Sala, pessoa):  # deve ter alguma forma de reduzir isso aqui...
        if isinstance(pessoa, Aluno):
            pessoa._setSala(Sala)
        if isinstance(pessoa, Servidor):
            pessoa._setSala(Sala)
        if isinstance(pessoa, Professor):
            pessoa._setSala(Sala)
        if isinstance(pessoa, Coordenador):
            pessoa._setSala(Sala)
        if isinstance(pessoa, Diretor):
            pessoa._setSala(Sala)
        return True
    
    def cadastrarEndereco(self, pessoa):
        endereco = Endereco(str(input("Digite o nome da rua: \n")),
                            str(input("Digite o nome do bairro: \n")),
                            int(input("Digite o número: \n")),
                            str(input("Digite o nome da cidade: \n")),
        )
        if isinstance(pessoa, Aluno):
            pessoa._setEndereco(endereco)
        if isinstance(pessoa, Servidor):
            pessoa._setEndereco(endereco)
        if isinstance(pessoa, Professor):
                pessoa._setEndereco(endereco)
        if isinstance(pessoa, Coordenador):
                pessoa._setEndereco(endereco)
        if isinstance(pessoa, Diretor):
            pessoa._setEndereco(endereco)
        return True
        
    def atualizarEndereco(self, pessoa):  
        pessoa._setEndereco(self.cadastrarEndereco())

    def buscarPessoa(self): 
        id_pessoa = str(input("Digite o nome do Aluno: \n"))
        tipo = int(input("Digite 0 se for aluno! digite 1 se for servidor!\n")) # não consegui pensar em nada melhor
        if tipo == 0:
            return self.buscarAluno(Aluno(id_pessoa, None))
        if tipo == 1:
            return self.buscarServidor(Servidor(id_pessoa, None))
    
    def buscarAluno(self, aluno_procurado):
        for aluno_atual in BaseDados.alunos:
            if aluno_atual._getNome() == aluno_procurado._getNome():  # ta certo isso?
                return aluno_atual, print("deu bom") 
        return None, print("deu ruim")
    
    def buscarServidor(self, servidor_procurado):
        for servidor_atual in BaseDados.servidores:
            if  servidor_atual._getNome()==servidor_procurado._getNome():
                return servidor_atual, print("deu bom")
        return None, print("deu ruim")
                
    def deletarBase(self):      
        BaseDados.alunos.clear()
        BaseDados.servidores.clear()
    
    
    # cenas dos próximos capítulos...

    def buscarCurso(self, id_curso):
        pass
    
    def buscarDisciplina(self, id_disciplina):
        pass
    
    def buscarSala(self, id_sala):
        pass
    
    def atualizarPessoa(self, id_pessoa, novos_dados):
        pass
    
    def atualizarCurso(self, id_curso, novos_dados):
        pass
    
    def atualizarDisciplina(self, id_disciplina, novos_dados):
        pass
    
    def atualizarSala(self, id_sala, novos_dados):
        pass
    
    def deletarPessoa(self, id_pessoa):
        pass
    
    def deletarCurso(self, id_curso):
        pass
    
    def deletarDisciplina(self, id_disciplina):
        pass
    
    def deletarSala(self, id_sala):
        pass
