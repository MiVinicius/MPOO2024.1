import time
import os
def telaDeCarregamento():
    os.system('cls')
    for i in range(100):
        bar = "#" * i + " " * (100 - i) 
        print("Carregando " + "[" + bar + "]")
        time.sleep(0.1)
        os.system('cls')
        
