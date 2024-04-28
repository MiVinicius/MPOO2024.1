
from ProjetoCadastro.Model.Endereco import Endereco

class EnderecoController:
    
    @staticmethod
    def cadastrarEndereco():
        endereco = Endereco(str(input("Digite o nome da rua: \n")),
                            str(input("Digite o nome do bairro: \n")),
                            int(input("Digite o número: \n")),
                            str(input("Digite o nome da cidade: \n")))
        return endereco
    
    @staticmethod
    def buscarEndereco(pessoa):
        return pessoa._getEndereco()
    
    @staticmethod
    def atualizarEndereco(endereco, pessoa):
        return pessoa._setEndereco(endereco)
    
    @staticmethod
    def deletarEndereco(endereco, pessoa):
        return pessoa._setEndereco(endereco)
    