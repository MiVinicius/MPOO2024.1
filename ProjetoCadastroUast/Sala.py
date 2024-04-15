class Sala():

    def __init__(self) -> None:
        self.salaNumero = None
        self.blocoNumero = None

    def cadastrarSala(self):
        salaNum = int(input("Digite o número da sala: "))
        blocoNum = int(input("Digite o número do bloco: "))
        if salaNum and blocoNum:
            self.setSalaNumero(salaNum)
            self.setBlocoNumero(blocoNum)
            print("Sala e bloco cadastrados com sucesso!")
            return self
        print("Sala e bloco não cadastrados!")
        return None
    
    def deletarSala(self):
        self.salaNumero = None
        self.blocoNumero = None
        print("Sala deletada com sucesso!") # se deletar vai ter que usar o setSala da Diciplina

    def setSalaNumero(self, salaNum):
        self.salaNumero = salaNum

    def setBlocoNumero(self, blocoNum):
        self.blocoNumero = blocoNum

    def getSalaNumero(self):
        return self.salaNumero
    
    def getBlocoNumero(self):
        return self.blocoNumero
    # essas funções estão aqui mais pra acesso rápido, já que seriam usadas realmente em uma interface