import Endereco, Curso, Disciplina, Sala


class Professor():

    def __init__(self) -> None:
        self.nome = None
        self.cpf = None
        self.endereco = None
        self.curso = None
        self.disciplina = None

    def cadastrarProfessor(self): # pode colocar nomes iguais
        profNome = str(input("Digite o nome do professor: "))
        self.setNome(profNome)
        cpf = str(input("Digite o cpf: \n"))
        self.setCpf(cpf)
        self.cadastrarEndereco()
        self.cadastrarCurso()
        self.cadastrarDisciplina()
        return print("Cadastro concluido!")
    
    def cadastrarEndereco(self):
        self.setEndereco(Endereco.Endereco().cadastrarEndereco())

    def cadastrarCurso(self):
        self.setCurso(Curso.Curso().cadastrarCurso())

    def cadastrarDisciplina(self):
        self.setDisciplina(Disciplina.Disciplina().cadastrarDisciplina())

    def mostrarEndereco(self):  # essa função deveria existir?
        return print(self.endereco)

    def setNome(self, profNome):
        self.nome = profNome
    
    def getNome(self):
        return self.nome

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self): # ja tem uma função pra mostrar o endereço
        return self.endereco

    def setCurso(self, curso):
        self.curso = curso

    def getCurso(self):
        return self.curso
    
    def setDisciplina(self, disciplina):
        self.disciplina = disciplina
    
    def getDisciplina(self):
        return self.disciplina

    def __repr__(self) -> str:  # garante que o nome seja mostrado em string legivel
        return f"Professor: {self.nome}, CPF: {self.cpf}"
        