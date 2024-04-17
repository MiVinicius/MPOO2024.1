from Aluno import Aluno
from Endereco import Endereco
from Curso import Curso
from Disciplina import Disciplina
from Professor import Professor
from Sala import Sala

# arquivo para testes

def testesAluno():

    print("===========================" * 6)
    aluno1 = Aluno()
    # aluno1.cadastrarAluno()
    aluno1.setNome("jill")
    aluno1.setMatricula("A001")

    endereco1 = Endereco()
    # endereco1.cadastrarEndereco()
    endereco1.setRua("rua 1")
    endereco1.setBairro("vila bela")
    endereco1.setNumero(110)
    endereco1.setCidade("serra talhada")
    aluno1.setEndereco(endereco1)

    curso1 = Curso()
    # curso1.cadastrarCurso()
    curso1.setNome("bsi")
    disciplina1 = Disciplina()
    # disciplina1.cadastrarDisciplina()
    disciplina1.setNome("MPOO")
    sala1 = Sala()
    # sala1.cadastrarSala()
    sala1.setSalaNumero(12)
    sala1.setBlocoNumero(2)
    disciplina1.setSala(sala1)
    curso1.setDisciplina(disciplina1)
    aluno1.setCurso(curso1)
    aluno1.setDisciplina(disciplina1)
    aluno1.getCurso().getDisciplinas()  

    print(aluno1)
    aluno1.mostrarEndereco()
    print(aluno1.getEndereco())
    print(aluno1.getNome())
    print(aluno1.getMatricula())
    print(aluno1.getCurso())
    print(aluno1.getDisciplina())
    print(aluno1.getCurso().getDisciplinas())  
    print("===========================" * 6)
    
def testesProfessor():
    print("===========================" * 6)
    professor1 = Professor()
    # professor1.cadastrarProfessor()
    professor1.setNome("luiz")

    endereco2 = Endereco()
    # endereco2.cadastrarEndereco()
    endereco2.setRua("rua 3")
    endereco2.setBairro("caxixola")
    endereco2.setNumero(9)
    endereco2.setCidade("serra talhada")

    curso2 = Curso()
    # curso2.cadastrarCurso()
    curso2.setNome("letras")
    disciplina2 = Disciplina()
    # disciplina2.cadastrarDisciplina()
    disciplina2.setNome("libras")
    sala2 = Sala()
    # sala2.cadastrarSala()
    sala2.setSalaNumero(3)
    sala2.setBlocoNumero(1)
    disciplina2.setSala(sala2)
    curso2.setDisciplina(disciplina2)
    professor1.setCurso(curso2)
    professor1.setDisciplina(disciplina2)
    professor1.getCurso().getDisciplinas() 

    print(professor1)
    print(professor1.getNome())
    print(professor1.getCurso())
    print(professor1.getDisciplina())
    print(professor1.getCurso().getDisciplinas()) 
    print("===========================" * 6)

def testesEndereco():
    print("===========================" * 6)
    endereco = Endereco()
    # endereco.cadastrarEndereco()
    endereco.setRua("Rua calango")
    endereco.setBairro("Bairro calango")
    endereco.setNumero(00)
    endereco.setCidade("Cidade calango")
    endereco.mostrarEndereco()
    endereco.deletarEndereco() # funciona!

    print("===========================" * 6)

def testesCurso():
    curso = Curso()
    # curso.cadastrarCurso()
    curso.setNome("eletronica")
    disciplina10 = Disciplina()
    disciplina10.setNome("matematica")
    sala55= Sala()
    sala55.setSalaNumero(67)
    sala55.setBlocoNumero(34)
    disciplina10.setSala(sala55)
    curso.setDisciplina(disciplina10)
    curso.mostrarCurso()
    curso.mostrarDisciplinas()
    curso.deletarCursos()

def testesDisciplina():
    print("===========================" * 6)
    disciplina3 = Disciplina()
    # disciplina3.cadastrarDisciplina()
    disciplina3.setNome("geografia")
    sala5= Sala()
    sala5.setSalaNumero(67)
    sala5.setBlocoNumero(34)
    disciplina3.setSala(sala5)
    disciplina3.mostrarDisciplina()
    disciplina3.deletarDisciplina() # funciona!

    print("===========================" * 6)
    
def testesSala():
    sala = Sala()
    # sala.cadastrarSala()
    sala.setSalaNumero(979)
    sala.setBlocoNumero(434)
    sala.mostrarSala()
    sala.deletarSala() # funciona!




testesAluno()
testesProfessor()
testesEndereco()
testesDisciplina()
testesSala()
testesCurso()




