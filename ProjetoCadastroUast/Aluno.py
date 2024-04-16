import Endereco, Curso, Disciplina, Sala


class Aluno(): 

    def __init__(self) -> None:  #vai criar o objeto, mas ele é vazio
        self.nome = None
        self.matricula = None
        self.endereco = None
        self.curso = None
        self.disciplinas = []

    def cadastrarAluno(self):  # vai cadastrar o aluno, requer varios cadastros
        nome = str(input("Digite o nome do aluno: \n"))
        self.setNome(nome)
        matricula = str(input("Digite a matricula do aluno: \n"))
        self.matricula(matricula)
        self.cadastrarEndereco(self)
        self.cadastrarCurso(self)
        self.cadastrarDisciplina(self)
        return print("cadastro do aluno concluido")
    
    def cadastrarEndereco(self):
        self.setEndereco(Endereco.Endereco().cadastrarEndereco())

    def cadastrarCurso(self):
        self.setCurso(Curso.Curso().cadastrarCurso())

    def cadastrarDisciplina(self):
        self.setDisciplina(Disciplina.Disciplina().cadastrarDisciplina())
    
    def mostrarEndereco(self):  # vai mostrar o endereço do aluno
        return print(self.endereco)
    
    def setNome(self, nome)-> None:  # vai colocar o nome no aluno
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setMatricula(self, matricula)-> None:
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setEndereco(self, endereco)-> None:  # vai colocar o endereço no aluno
        self.endereco = endereco

    def getEndereco(self): # ja tem uma função pra mostrar o endereço
        return self.endereco

    def setCurso(self, curso)-> None:
        self.curso = curso
    
    def getCurso(self):
        return self.curso

    def setDisciplina(self, disciplina)-> None:
        self.disciplinas.append(disciplina)

    def getDisciplina(self):
        return self.disciplinas   
    
    def __repr__(self) -> str:  # garante que o nome seja mostrado em string legivel
        return f"Aluno: {self.nome}, Matricula: {self.matricula}"

