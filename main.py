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

    def ajustarVolume(self, volume):  # ajusta o volume, o volume tem que ser maior ou igual a 0 (zero)
        if volume >= 0:
            print(f"Volume alterado para {volume}")
            self.volume = volume
        else:
            print("Volume não pode ser negativo.")

    def ajustarCanal(self, canal):  # ajusta o canal, tem que ser maior que 0 (zero)
        if canal > 0:
            print(f"Canal mudou para {canal}")
            self.canal = canal
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
televisao.ajustarVolume(5)
televisao.mudo()
televisao.ajustarCanal(10)
televisao.obterInformacao()
