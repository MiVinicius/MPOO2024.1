# programa para representar uma Televisão (da forma que eu entendi)
class Televisao:
    def __init__(self):  # inicializa a Televisão
        self.energia = False
        self.canal = 1
        self.volume = 0

    def on(self):  # liga a Televisão
        if self.energia == False:
            print("A TV vai ligar")
            self.energia = True

    def off(self):  # desliga a Televisão
        if self.energia == True:
            print("A TV vai desligar")
            self.energia = False

    def volumeAcima(self):  # aumenta o volume da TV
        if self.volume >= 0:
            print(f"Volume alterado para {self.volume+1}")
            self.volume = self.volume+1
        else:
            print("Volume não pode ser menor que Zero.")

    def volumeAbaixo(self):  # diminui o volume da TV
        if self.volume < 100:
            print(f"Volume alterado para {self.volume-1}")
            self.volume = self.volume-1
        else:
            print("Volume não pode ser maior que 100.")

    def canalAcima(self):  # muda o número do canal para cima, não pode ser 100
        if self.canal < 100:
            print(f"Canal mudou para {self.canal+1}")
            self.canal = self.canal+1
        else:
            print("Número de canal inválido.")

    def canalAbaixo(self):  # muda o número do canal para baixo, não pode ser 0 (zero)
        if self.canal > 0:
            print(f"Canal mudou para {self.canal-1}")
            self.canal = self.canal-1
        else:
            print("Número de canal inválido.")

    def mudo(self):  # reduz o volume a 0 (zero)
        print("Volume mutado.")
        self.volume = 0

    def obterInformacao(self):  # deveria fazer alguma coisa, algum dia...
        print("Obtendo informação do canal... Erro! Cabo da antena não conectado!")


# testes, o console vai mostrar as saidas


televisao = Televisao()
televisao.on()
televisao.off()
televisao.volumeAcima()
televisao.volumeAbaixo()
televisao.mudo()
televisao.canalAcima()
televisao.canalAbaixo()
televisao.obterInformacao()
