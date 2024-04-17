from Disciplina import Disciplina

class Curso():

    def __init__(self) -> None:
        self.__nome = None
        self.__disciplinas = []  
        
    def cadastrarCurso(self):
        nome = str(input("Digite o nome do curso: \n"))
        self.setNome(nome)
        print("Curso cadastrado com sucesso!")
        return self
    
    def cadastrarDisciplina(self):
        self.setDisciplina(Disciplina().cadastrarDisciplina())
    
    def deletarCursos(self): # envia os cursos pras cucuias
        self.__nome = None
        self.__disciplinas = None
        print("Cursos deletados com sucesso!")
        
    def mostrarCurso(self):
        return print(self.getNome())
    
    def mostrarDisciplinas(self):
        return print(self.getDisciplinas())

    def setNome(self, nome):
        self.__nome = nome

    def setDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def getNome(self):
        return self.__nome
    
    def getDisciplinas(self):
        return self.__disciplinas
    
    def __repr__(self) -> str:
        return f"curso(s): {self.__nome}"
