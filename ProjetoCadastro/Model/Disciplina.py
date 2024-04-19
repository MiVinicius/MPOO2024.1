
class Disciplina():
    
    def __init__(self, nome, sala) -> None:
        self.__nome = nome
        self.__sala = sala
        
    def _mostrarDados(self):
        print(repr)
    
    def _setNome(self, disciplina):
        self.__nome = disciplina

    def _setSala(self, sala):
        self.__sala = sala

    def _getSala(self):
        return self.__sala
    
    def _getNome(self):
        return self.__nome
    
    def __repr__(self) -> str:
        return f"Disciplina: {self.__nome}, {self.__sala}"