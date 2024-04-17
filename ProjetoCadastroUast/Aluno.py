from Endereco import Endereco
from Curso import Curso
from Disciplina import Disciplina

class Aluno(): 

    def __init__(self) -> None:  #vai criar o objeto, mas ele é vazio
        self.__nome = None
        self.__matricula = None
        self.__endereco = None
        self.__curso = None
        self.__disciplinas = []

    def cadastrarAluno(self):  # vai cadastrar o aluno, requer varios cadastros
        nome = str(input("Digite o nome do aluno: \n"))
        self.setNome(nome)
        matricula = str(input("Digite a matricula do aluno: \n"))
        self.setMatricula(matricula)
        self.cadastrarEndereco()
        self.cadastrarCurso()
        self.cadastrarDisciplina()
        return print("cadastro concluido, ", self, self.getCurso(), self.getEndereco())
    
    def cadastrarEndereco(self):
        self.setEndereco(Endereco().cadastrarEndereco())

    def cadastrarCurso(self):
        self.setCurso(Curso().cadastrarCurso())

    def cadastrarDisciplina(self):
        self.setDisciplina(Curso.cadastrarDisciplina(self))
    
    def mostrarEndereco(self):  # vai mostrar o endereço do aluno
        return print(self.__endereco)
    
    def deletarAluno(self): 
        del self
    
    def setNome(self, nome)-> None:  # vai colocar o nome no aluno
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def setMatricula(self, matricula)-> None:
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def setEndereco(self, endereco)-> None:  # vai colocar o endereço no aluno
        self.__endereco = endereco

    def getEndereco(self): # ja tem uma função pra mostrar o endereço
        return self.__endereco

    def setCurso(self, curso)-> None:
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso

    def setDisciplina(self, disciplina)-> None:
        self.__disciplinas.append(disciplina)

    def getDisciplina(self):
        return self.__disciplinas   
    
    def __repr__(self) -> str:  # garante que o nome seja mostrado em string legivel
        return f"Aluno: {self.__nome}, Matricula: {self.__matricula}"

