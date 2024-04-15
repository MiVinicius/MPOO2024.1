import Disciplina


class Curso():

    def __init__(self) -> None:
        self.nome = None
        self.cursos = []  # mais facil de retornar os nomes depois
        self.disciplinas = []   # mesma coisa
        #self.professor = [] # e foi nesse momento que eu pensei, estou perdido no que fazer nesse projeto
        
    def cadastrarCurso(self):
        nome = str(input("Digite o nome do curso: \n"))
        if nome:
            self.setNome(nome)
            self.cursos.append(nome)
            print("Curso cadastrado com sucesso!")
            return self
        print("curso não cadastrado!")
        return None
    
    def buscarCurso(self, cursoBuscar):
        for curso in self.cursos:
            if curso == cursoBuscar:
                return curso
        return None
    
    def cadastrarDisciplina(self):
        self.setDiciplina(Disciplina.Disciplina().cadastrarDisciplina())
    
    def deletarCursos(self): # envia os cursos pras cucuias
        self.nome = None
        self.diciplinas = None
        self.cursos = None
        print("Cursos deletados com sucesso!")

    def mostrarCursos(self):
        return self.cursos
    
    def mostrarDiciplinas(self):
        return self.diciplinas

    def setNome(self, nome):
        self.nome = nome

    def setDiciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def getNome(self):
        return self.nome

    def getCursos(self):
        return self.cursos
    
    def getDiciplinas(self):
        return self.diciplinas
