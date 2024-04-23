
class Sala():

    def __init__(self, numero, bloco) -> None:
        self.__numero = numero
        self.__bloco = bloco
        
    def _mostrarDados(self):
        print(self.__repr__())
        
    def _setSalaNumero(self, salaNum):
        self.__numero = salaNum

    def _setBlocoNumero(self, blocoNum):
        self.__bloco = blocoNum

    def _getSalaNumero(self):
        return self.__numero
    
    def _getBlocoNumero(self):
        return self.__bloco
    
    def __repr__(self) -> str:
        return f"Sala: {self.__numero}, Bloco: {self.__bloco}"