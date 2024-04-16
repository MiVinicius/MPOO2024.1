class Endereco():

    def __init__(self) -> None:
        self.rua = None
        self.bairro = None
        self.numero = None
        self.cidade = None

    def cadastrarEndereco(self):  # é só não colocar nada na entrada que dá bom
        rua = str(input("Digite o nome da rua: \n"))
        if rua:
            Endereco.setRua(self, rua)
        bairro = str(input("Digite o nome do bairro: \n"))
        if bairro: 
            Endereco.setBairro(self, bairro)
        numero = int(input("Digite o nome do numero: \n"))
        if numero:
            Endereco.setNumero(self, numero)
        cidade = str(input("Digite o nome da cidade: \n"))
        if cidade:
            Endereco.setCidade(self, cidade)
        print("cadastro do endereço concluido")
        return self
    
    def deletarEndereco(self):  # se chamar com algum professor ou aluno, o endereço vai a None
        self.rua = None
        self.bairro = None
        self.numero = None
        self.cidade = None
        print("Endereço deletado com sucesso.")

    def mostrarEndereco(self):  # retorna a função de baixo para mostrar os dados em caso de instancia desta classe sozinha, print também serve
        return print(self.__repr__())

    def setRua(self, rua):
        self.rua = rua

    def setBairro(self, bairro):
        self.bairro = bairro

    def setNumero(self, numero):
        self.numero = numero

    def setCidade(self, cidade):
        self.cidade = cidade

    def getRua (self):
        return self.rua
    
    def getBairro(self):
        return self.bairro
    
    def getNumero(self):
        return self.numero
    
    def getCidade(self):
        return self.cidade

    def __repr__(self) -> str:
        return f"Rua: {self.rua}, Bairro: {self.bairro}, Número: {self.numero}, Cidade: {self.cidade}"