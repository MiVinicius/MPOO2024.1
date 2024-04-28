from Model.BaseDados import BaseDados
from View.MenuView import Menu


""" 
Projeto de melhora continua
"""

def Main():
    
    # iniciar bateria de testes! cadastros dentro da base de dados
    baseDados = BaseDados()
    baseDados.inicializarBase()
    Menu()
    
    
    
    # testes de cadastro, pra saber se dá erro (erro = false no terminal)
    # print(baseDados.cadastrarPessoa(Aluno("Carlos", "445.465.465.04")))
    # print(baseDados.cadastrarPessoa(Aluno("Carlos", "445.465.465.04")))
    # print(baseDados.cadastrarPessoa(Servidor("Geronimo", "627.628.635-98")))
    # print(baseDados.cadastrarPessoa(Servidor("Geronimo", "627.628.635-98")))
    # print(baseDados.cadastrarPessoa(Professor("João", "164.646.756-79")))
    # print(baseDados.cadastrarPessoa(Professor("João", "164.646.756-79")))
    
    
    # baseDados.cadastrarPessoa(Coordenador("Jose", "956.393.347.32"))
    # baseDados.cadastrarPessoa(Coordenador("Jose", "956.393.347.32"))
    # baseDados.cadastrarPessoa(Diretor("Leonardo", "555.555.555-55"))
    # baseDados.cadastrarPessoa(Diretor("Leonardo", "555.555.555-55"))
    
    
    
    # testes de busca, funciona
    # print(baseDados.buscarPessoaExiste("Carlos"))
    # print(baseDados.buscarPessoaExiste("Geronimo"))
    # print(baseDados.buscarPessoaExiste("João"))
    # print(baseDados.buscarPessoaExiste("Leonardo"))
    # print(baseDados.buscarPessoaExiste("Jose"))
    
    
    # baseDados.listarAlunos()
    # aluno = Aluno("Misael", "999")
    # print(aluno)
    # aluno._mostrarDados()
    # print(aluno)
    # print(aluno._getNome())
    
    # servidor = Servidor("Geronimo", "627.628.635-98")
    # baseDados.cadastrarPessoa(servidor)
    # servidor._mostrarDados()
    # print(servidor)
    
    # professor = Professor("Julian", "124.735.846-72")
    # baseDados.cadastrarPessoa(professor)
    
    # coordenador = Coordenador("Túlio", "034.346.786-04")
    # baseDados.cadastrarPessoa(coordenador)
    
    # diretor = Diretor("Mauricio", "405.695.954-60")
    # baseDados.cadastrarPessoa(diretor)
    
    
    # testes endereco
    # endereco = Endereco("Rua calango", "Bairro calango", 00, "Cidade calango", "Estado Calango")
    # endereco._mostrarDados()
    # baseDados.passarEndereco(endereco, aluno)
    # aluno._mostrarDados()
    
    
    
if __name__ == "__main__":
    Main()





