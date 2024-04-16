import Sala

class Disciplina():
    
    def __init__(self) -> None:
        self.nome = None
        self.sala = None

    def cadastrarDisciplina(self):
        disciplina = str(input("Digite o nome da disciplina: "))
        if disciplina:
            self.setNome(disciplina)
            self.cadastrarSala() 
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
    
    def __repr__(self) -> str:
        return f"Disciplina: {self.nome}, {self.sala}"
        