import Sala

class Disciplina():
    
    def __init__(self) -> None:
        self.nome = None
        self.sala = None

    def cadastrarDisciplina(self):
        disciplina = str(input("Digite o nome da disciplina: "))
        if disciplina:
            self.setNome(disciplina)
            self.cadastrarSala() # vou obrigar colocar a sala e o bloco no cadastro da diciplina, 
                                 # para que fique igual o sigaa que a sala que colocam é a sala errada
            print("Diciplina cadastrada com sucesso!")
            return self
        print("Disciplina não cadastrada")
        return None

    def cadastrarSala(self):
        self.setSala(Sala.Sala().cadastrarSala())

    def deletarDisciplina(self):
        self.nome = None
        self.sala = None
        print("Disciplina deletada com sucesso!")

    def setNome(self, disciplina):
        self.nome = disciplina

    def setSala(self, sala):
        self.sala = sala

    def getSala(self):
        return self.sala
    
    def getNome(self):
        return self.nome
        