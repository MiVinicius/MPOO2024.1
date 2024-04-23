
class Servidor():
    
    def __init__(self, nome, cpf) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = None
    
    def _mostrarDados(self):
        print(repr)
        
    def _getNome(self):
        return self.__nome
    
    def _setNome(self, nome):
        self.__nome = nome
    
    def _getCpf(self):
        return self.__cpf
    
    def _setCpf(self, cpf):
        self.__cpf = cpf
        
    def _getEndereco(self):
        return self.__endereco
    
    def _setEndereco(self, endereco):
        self.__endereco = endereco
    
    def __repr__(self) -> str:
        f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}"