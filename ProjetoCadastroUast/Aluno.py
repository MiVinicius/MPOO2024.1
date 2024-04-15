import Endereco, Curso, Disciplina, Sala


class Aluno(): 

    def __init__(self) -> None:  #vai criar o objeto, mas ele é vazio
        self.nome = None
        self.endereco = None
        self.curso = None
        self.disciplina = None
        self.sala = None
        self.alunos = []  # nosso armazenamento será list

    def cadastrarAluno(self):  # vai cadastrar o aluno - aceita string
        nome = str(input("Digite o nome do aluno: \n"))
        self.setNome(nome)
        # self.alunos.append(nome)  deveria ficar aqui, foi implementada no setNome
        return print("cadastro do aluno concluido")
    
    def buscarAluno(self, alunoBuscar):  # retorna o nome do aluno - aceita string
        for aluno in self.alunos:
            if aluno == alunoBuscar:
                return aluno
        return None
    
    def mudarNomeAluno(self, nomeAntigo, nomeNovo): # utiliza do metodo index da list para alterar o nome do aluno
        if self.buscarAluno(nomeAntigo):
            indice = self.alunos.index(nomeAntigo)
            self.alunos[indice] = nomeNovo
            print("Nome do aluno alterado com sucesso! ")
            return True
        return False
    
    def deletarAluno(self, alunoDeletar):  # vai remover o aluno da list do sistema
        if self.buscarAluno(alunoDeletar):
            self.alunos.remove(alunoDeletar)
            print("aluno deletado do sistema com sucesso!")
            return True
        return False
    
    def mostrarEndereco(self):  # vai mostrar o endereço do aluno
        return self.endereco
    
    def mostrarAlunos(self):  # vai mostrar todos os alunos cadastrados, será que essa função é realmente necessária?
        return self.alunos
    
    def setNome(self, nome)-> None:  # vai colocar o nome no aluno
        self.nome = nome
        self.alunos.append(nome)  # usada para os testes funcionarem

    def setEndereco(self)-> None:  # vai colocar o endereço no aluno
        self.endereco = Endereco.Endereco().cadastrarEndereco()

    def setCurso(self):
        self.curso = Curso.Curso().cadastrarCurso()
    
    def setDisciplina(self):
        self.disciplina = Disciplina.Disciplina().cadastrarDisciplina()
    
    def setSala(self):
        self.sala = Sala.Sala().cadastrarSala()
    
    def __repr__(self) -> str:  # garante que o nome seja mostrado em string legivel
        return f"Aluno: {self.nome}"

