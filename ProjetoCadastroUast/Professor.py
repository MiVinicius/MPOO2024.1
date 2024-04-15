import Endereco, Curso, Disciplina, Sala


class Professor():

    def __init__(self) -> None:
        self.nome = None
        self.endereco = None
        self.curso = None
        self.disciplina = None
        self.sala = None
        self.professores = []  # professores aqui

    def cadastrarProfessor(self): # pode colocar nomes iguais
        profNome = str(input("Digite o nome do professor: "))
        self.setNome(profNome)
        # self.professores.append(profNome)  implementada no setNome
        return print("Cadastro concluido!")

    def buscarProfessor(self, professorBuscar):  # retorna o nome do professor - aceita string
        for professor in self.professores:
            if professor == professorBuscar:
                return professor
        return None
    
    def mudarNomeProfessor(self, nomeAntigo, nomeNovo):  # utiliza do metodo index da list para alterar o nome do professor
        if self.buscarProfessor(nomeAntigo):
            indice = self.professores.index(nomeAntigo)
            self.professores[indice] = nomeNovo
            print("Nome do professor alterado com sucesso!")
            return True
        return False
    
    def deletarProfessor(self, professorDeletar):  # vai remover o professor da list do sistema
        if self.buscarProfessor(professorDeletar):
            self.professores.remove(professorDeletar)
            print("professor deletado do sistema com sucesso!")
            return True
        return False

    def mostrarProfessores(self):  # vai mostrar todos os alunos cadastrados, será que essa função é realmente necessária?
        return self.professores

    def mostrarEndereco(self):  # vai mostrar o endereço do aluno
        return self.endereco

    def setNome(self, profNome):
        self.nome = profNome
        self.professores.append(profNome)  # usada  para os testes funcionarem
    
    def setEndereco(self):
        self.endereco = Endereco.Endereco().cadastrarEndereco()

    def setCurso(self):
        self.curso = Curso.Curso().cadastrarCurso()
    
    def setDisciplina(self):
        self.disciplina = Disciplina.Disciplina().cadastrarDisciplina()
    
    def setSala(self):
        self.sala = Sala.Sala().cadastrarSala()
    
    def __repr__(self) -> str:  # garante que o nome seja mostrado em string legivel
        return f"Professor: {self.nome}"
        