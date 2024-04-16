import Endereco, Curso, Disciplina, Sala


class Professor():

    def __init__(self) -> None:
        self.nome = None
        self.endereco = None
        self.curso = None
        self.disciplina = None

    def cadastrarProfessor(self): # pode colocar nomes iguais
        profNome = str(input("Digite o nome do professor: "))
        self.setNome(profNome)
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

    def mostrarEndereco(self):  # vai mostrar o endereço do professor
        return print(self.endereco)

    def setNome(self, profNome):
        self.nome = profNome
    
    def setEndereco(self, endereco):
        self.endereco = endereco

    def setCurso(self, curso):
        self.curso = curso
    
    def setDisciplina(self, disciplina):
        self.disciplina = disciplina
    
    def __repr__(self) -> str:  # garante que o nome seja mostrado em string legivel
        return f"Professor: {self.nome}"
        