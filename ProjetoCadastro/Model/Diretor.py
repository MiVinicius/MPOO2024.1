from Coordenador import Coordenador

class Diretor(Coordenador):
    
    def __init__(self, nome, cpf, universidade=None):
        super().__init__(nome, cpf)
        self.__universidade = universidade
        self.__endereco = None
        
    def _mostrarDados(self):
        return print(self.__repr__())
        
    def _getNome(self):
        return super()._getNome()
    
    def _setNome(self, nome):
        super()._setNome(nome)
        
    def _getCpf(self):
        return super()._getCpf()
    
    def _setCpf(self, cpf):
        super()._setCpf(cpf)
        
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
            return super().__eq__(other) and self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
        
    def __repr__(self):
        return f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}, Diretor da Universidade: {self.__universidade}"