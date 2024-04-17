from Sala import Sala

class Disciplina():
    
    def __init__(self) -> None:
        self.__nome = None
        self.__sala = None

    def cadastrarDisciplina(self):
        disciplina = str(input("Digite o nome da disciplina: \n"))
        self.setNome(disciplina)
        self.cadastrarSala() 
        print("Diciplina cadastrada com sucesso!")
        return self

    def cadastrarSala(self):
        self.setSala(Sala().cadastrarSala())

    def deletarDisciplina(self):
        self.__nome = None
        self.__sala = None
        print("Disciplina deletada com sucesso!")

    def setNome(self, disciplina):
        self.__nome = disciplina

    def setSala(self, sala):
        self.__sala = sala

    def getSala(self):
        return self.__sala
    
    def getNome(self):
        return self.__nome
    
    def __repr__(self) -> str:
        return f"Disciplina: {self.__nome}, {self.__sala}"
        