import sys
sys.path.append('.')
from ProjetoCadastro.Model.BaseDadosModel import BaseDadosModel
from ProjetoCadastro.View.MenuView import MenuView
# from Controller.BaseDadosController import BaseDadosController

""" 
Projeto de melhora continua
"""

def Main():
    
    # cadastros dentro da base de dados
    
    # BaseDados().inicializarBase() # não funciona 
    
    BaseDadosModel()  # funciona
    
    
    MenuView()
    
    
    
    
    
    
    
if __name__ == "__main__":
    Main()





