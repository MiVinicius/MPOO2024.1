class Sala():

    def __init__(self) -> None:
        self.__numero = None
        self.__bloco = None

    def cadastrarSala(self):
        salaNum = int(input("Digite o número da sala: \n"))
        blocoNum = int(input("Digite o número do bloco: \n"))
        self.setSalaNumero(salaNum)
        self.setBlocoNumero(blocoNum)
        print("Sala e bloco cadastrados com sucesso!")
        return self
    
    def deletarSala(self):
        self.__numero = None
        self.__bloco = None
        print("Sala deletada com sucesso!") 

    def setSalaNumero(self, salaNum):
        self.__numero = salaNum

    def setBlocoNumero(self, blocoNum):
        self.__bloco = blocoNum

    def getSalaNumero(self):
        return self.__numero
    
    def getBlocoNumero(self):
        return self.__bloco
    
    def __repr__(self) -> str:
        return f"Sala: {self.__numero}, Bloco: {self.__bloco}"