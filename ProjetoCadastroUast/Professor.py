from Curso import Curso

class Professor():

    def __init__(self) -> None:
        self.__nome = None
        self.__curso = None
        self.__disciplinas = []

    def cadastrarProfessor(self): 
        profNome = str(input("Digite o nome do professor: \n"))
        self.setNome(profNome)
        self.cadastrarCurso()
        self.cadastrarDisciplina()
        print("===========================" * 6)
        return print("Cadastro concluido, ", self, self.getCurso(), self.getDisciplina())

    def cadastrarCurso(self):
        self.setCurso(Curso().cadastrarCurso())

    def cadastrarDisciplina(self):
        self.setDisciplina(Curso.cadastrarDisciplina(self))

    def deletarProfessor(self):
        del self
    
    def setNome(self, profNome):
        self.__nome = profNome
    
    def getNome(self):
        return self.__nome

    def setCurso(self, curso):
        self.__curso = curso

    def getCurso(self):
        return self.__curso
    
    def setDisciplina(self, disciplina):  # por algum motivo isso retona um None adicional...
        self.__disciplinas.append(disciplina)

    def getDisciplina(self):
        return self.__disciplinas

    def __repr__(self) -> str:  
        return f"Professor: {self.__nome}, Curso: {self.__curso}, Disciplina(s): {self.__disciplinas}"
        