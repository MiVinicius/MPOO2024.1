from Endereco import Endereco
from Curso import Curso
from Disciplina import Disciplina

class Professor():

    def __init__(self) -> None:
        self.__nome = None
        self.__cpf = None
        self.__endereco = None
        self.__curso = None
        self.__disciplina = None

    def cadastrarProfessor(self): # pode colocar nomes iguais
        profNome = str(input("Digite o nome do professor: \n"))
        self.setNome(profNome)
        cpf = str(input("Digite o __cpf: \n"))
        self.setCpf(cpf)
        self.cadastrarEndereco()
        self.cadastrarCurso()
        self.cadastrarDisciplina()
        return print("Cadastro concluido!")
    
    def cadastrarEndereco(self):
        self.setEndereco(Endereco().cadastrarEndereco())

    def cadastrarCurso(self):
        self.setCurso(Curso().cadastrarCurso())

    def cadastrarDisciplina(self):
        self.setDisciplina(Disciplina().cadastrarDisciplina())

    def mostrarEndereco(self):  # essa função deveria existir?
        return print(self.__endereco)

    def deletarProfessor(self):
        del self
        print("professor foi pras cucuias")
    
    def setNome(self, profNome):
        self.__nome = profNome
    
    def getNome(self):
        return self.__nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getEndereco(self): # ja tem uma função pra mostrar o endereço
        return self.__endereco

    def setCurso(self, curso):
        self.__curso = curso

    def getCurso(self):
        return self.__curso
    
    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina
    
    def getDisciplina(self):
        return self.__disciplina

    def __repr__(self) -> str:  # garante que o nome seja mostrado em string legivel
        return f"Professor: {self.__nome}, CPF: {self.__cpf}"
        