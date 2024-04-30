from Model.BaseDados import BaseDados
from View.MenuView import MenuView
# from Controller.BaseDadosController import BaseDadosController

""" 
Projeto de melhora continua
"""

def Main():
    
    # cadastros dentro da base de dados
    
    # BaseDados().inicializarBase() # não funciona 
    
    BaseDados()  # funciona
    
    
    MenuView()
    
    
    
    
    
    
    
if __name__ == "__main__":
    Main()





