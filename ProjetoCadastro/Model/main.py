
from BaseDados import BaseDados
from Aluno import Aluno
# from Professor import Professor
# from Coordenador import Coordenador
# from Diretor import Diretor
# from Servidor import Servidor
from Endereco import Endereco
# from Disciplina import Disciplina
# from Sala import Sala
# from Curso import Curso
""" 
Projeto de melhora continua
"""

def Menu():
    baseDados = BaseDados()
    baseDados.inicializarBase()
    # baseDados.buscarAluno(Aluno("Misael", "999"))
    # baseDados.buscarPessoa()
    # baseDados.cadastrarPessoa()
    # baseDados.cadastrarAluno()
    # baseDados.inicializarBase()
    
    
    aluno = Aluno("Misael", "999")
    baseDados.cadastrarPessoa(aluno)
    # b = baseDados.buscarAluno(aluno)
    # aluno._mostrarDados()
    # print(aluno)
    # print(aluno._getNome())
    # servidor = Servidor("Geronimo", "627.628.635-98")
    # baseDados.cadastrarPessoa(servidor)
    # servidor._mostrarDados()
    # print(servidor)
    # professor = Professor("Julian", "124.735.846-72")
    # print(baseDados.cadastrarPessoa(professor))
    
    # coordenador = Coordenador("Gean", "034.346.786-74")
    # print(baseDados.cadastrarPessoa(coordenador))
    
    # diretor = Diretor("Mauro", "405.695.954-60")
    # print(baseDados.cadastrarPessoa(diretor))
    
    endereco = Endereco("Rua calango", "Bairro calango", 00, "Cidade calango", "Estado Calango")
    # endereco._mostrarDados()
    baseDados.passarEndereco(endereco, aluno)
    
    
    
    
Menu()





