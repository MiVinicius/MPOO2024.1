class Endereco():

    def __init__(self) -> None:
        self.__rua = None
        self.__bairro = None
        self.__numero = None
        self.__cidade = None

    def cadastrarEndereco(self):  
        rua = str(input("Digite o nome da rua: \n"))
        Endereco.setRua(self, rua)
        bairro = str(input("Digite o nome do bairro: \n"))
        Endereco.setBairro(self, bairro)
        numero = int(input("Digite o número: \n"))
        Endereco.setNumero(self, numero)
        cidade = str(input("Digite o nome da cidade: \n"))
        Endereco.setCidade(self, cidade)
        print("cadastro do endereço concluido")
        return self
    
    def deletarEndereco(self):  # se chamar com algum professor ou aluno, o endereço vai a None
        self.__rua = None
        self.__bairro = None
        self.__numero = None
        self.__cidade = None
        print("Endereço deletado com sucesso.")

    def mostrarEndereco(self):  
        return print(self.__repr__())

    def setRua(self, rua):
        self.__rua = rua

    def setBairro(self, bairro):
        self.__bairro = bairro

    def setNumero(self, numero):
        self.__numero = numero

    def setCidade(self, cidade):
        self.__cidade = cidade

    def getRua (self):
        return self.__rua
    
    def getBairro(self):
        return self.__bairro
    
    def getNumero(self):
        return self.__numero
    
    def getCidade(self):
        return self.__cidade

    def __repr__(self) -> str:
        return f"Rua: {self.__rua}, Bairro: {self.__bairro}, Número: {self.__numero}, Cidade: {self.__cidade}"