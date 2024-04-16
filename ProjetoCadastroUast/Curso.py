import Disciplina


class Curso():

    def __init__(self) -> None:
        self.nome = None
        self.disciplinas = []  
        
    def cadastrarCurso(self):
        nome = str(input("Digite o nome do curso: \n"))
        if nome:
            self.setNome(nome)
            print("Curso cadastrado com sucesso!")
            return self
        print("curso não cadastrado!")
        return None
    
    def cadastrarDisciplina(self):
        self.setDisciplina(Disciplina.Disciplina().cadastrarDisciplina())
    
    def deletarCursos(self): # envia os cursos pras cucuias
        self.nome = None
        self.disciplinas = None
        print("Cursos deletados com sucesso!")
    
    def mostrarDisciplinas(self):
        return self.disciplinas

    def setNome(self, nome):
        self.nome = nome

    def setDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def getNome(self):
        return self.nome
    
    def getDiciplinas(self):
        return self.disciplinas
