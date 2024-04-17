from Endereco import Endereco
from Curso import Curso

class Aluno(): 

    def __init__(self) -> None:  
        self.__nome = None
        self.__matricula = None
        self.__endereco = None
        self.__curso = None
        self.__disciplinas = []

    def cadastrarAluno(self):  
        nome = str(input("Digite o nome do aluno: \n"))
        self.setNome(nome)
        matricula = str(input("Digite a matricula do aluno: \n"))
        self.setMatricula(matricula)
        self.cadastrarEndereco()
        print("===========================" * 6)
        return print("cadastro concluido, ", self)
    
    def cadastrarEndereco(self):
        self.setEndereco(Endereco().cadastrarEndereco())

    def cadastrarCurso(self):
        self.setCurso(Curso().cadastrarCurso())

    def cadastrarDisciplina(self):
        self.setDisciplina(Curso.cadastrarDisciplina(self))
    
    def mostrarEndereco(self):  
        return print(self.__endereco)
    
    def deletarAluno(self): 
        del self
    
    def setNome(self, nome)-> None: 
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def setMatricula(self, matricula)-> None:
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def setEndereco(self, endereco)-> None:  
        self.__endereco = endereco

    def getEndereco(self): 
        return self.__endereco

    def setCurso(self, curso)-> None:
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso

    def setDisciplina(self, disciplina):  # por algum motivo isso retona um None adicional...
        self.__disciplinas.append(disciplina)

    def getDisciplina(self):
        return self.__disciplinas   
    
    def __repr__(self) -> str:  
        return f"Aluno: {self.__nome}, Matricula: {self.__matricula}"

