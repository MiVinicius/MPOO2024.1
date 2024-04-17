class Sala():

    def __init__(self) -> None:
        self.__salaNumero = None
        self.__blocoNumero = None

    def cadastrarSala(self):
        salaNum = int(input("Digite o número da sala: \n"))
        blocoNum = int(input("Digite o número do bloco: \n"))
        if salaNum and blocoNum:
            self.setSalaNumero(salaNum)
            self.setBlocoNumero(blocoNum)
            print("Sala e bloco cadastrados com sucesso!")
            return self
        print("Sala e bloco não cadastrados!")
        return None
    
    def deletarSala(self):
        self.__salaNumero = None
        self.__blocoNumero = None
        print("Sala deletada com sucesso!") 

    def setSalaNumero(self, salaNum):
        self.__salaNumero = salaNum

    def setBlocoNumero(self, blocoNum):
        self.__blocoNumero = blocoNum

    def getSalaNumero(self):
        return self.__salaNumero
    
    def getBlocoNumero(self):
        return self.__blocoNumero
    
    def __repr__(self) -> str:
        return f"Sala: {self.__salaNumero}, Bloco: {self.__blocoNumero}"