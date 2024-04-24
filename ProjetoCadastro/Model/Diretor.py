from Coordenador import Coordenador

class Diretor(Coordenador):
    
    def __init__(self, nome, cpf, universidade=None):
        super().__init__(nome, cpf)
        self.__universidade = universidade
        self.__endereco = None
        
    def _mostrarDados(self):
        return print(self.__repr__())
        
    # def _getNome(self):
    #     return self.__nome
    
    # def _setNome(self, nome):
    #     self.__nome = nome
        
    # def _getCpf(self):
    #     return self.__cpf
    
    # def _setCpf(self, cpf):
    #     self.__cpf = cpf
        
    def _getUnivesidade(self):
        return self.__universidade
    
    def _setUniversidade(self, universidade):
        self.__universidade = universidade
    
    def _getEndereco(self):
        return self.__endereco
    
    def _setEndereco(self, endereco):
        self.__endereco = endereco
        
    def __eq__(self, other):
        if isinstance(other, Diretor):
            return self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
        
    def __repr__(self):
        return f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}, Diretor da Universidade: {self.__universidade}"