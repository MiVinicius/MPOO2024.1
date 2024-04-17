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
    aluno1.setNome("jill")
    aluno1.setMatricula("A001")

    endereco1 = Endereco()
    endereco1.setRua("rua 1")
    endereco1.setBairro("vila bela")
    endereco1.setNumero(110)
    endereco1.setCidade("serra talhada")
    aluno1.setEndereco(endereco1)

    curso1 = Curso()
    curso1.setNome("bsi")
    disciplina1 = Disciplina()
    disciplina1.setNome("MPOO")
    sala1 = Sala()
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
    professor1.setNome("luiz")
    professor1.setCpf("12345678910")

    endereco2 = Endereco()
    endereco2.setRua("rua 3")
    endereco2.setBairro("caxixola")
    endereco2.setNumero(9)
    endereco2.setCidade("serra talhada")
    professor1.setEndereco(endereco2)

    curso2 = Curso()
    curso2.setNome("letras")
    disciplina2 = Disciplina()
    disciplina2.setNome("libras")
    sala2 = Sala()
    sala2.setSalaNumero(3)
    sala2.setBlocoNumero(1)
    disciplina2.setSala(sala2)
    curso2.setDisciplina(disciplina2)
    professor1.setCurso(curso2)
    professor1.setDisciplina(disciplina2)
    professor1.getCurso().getDisciplinas() 

    print(professor1)
    professor1.mostrarEndereco() 
    print(professor1.getEndereco())
    print(professor1.getNome())
    print(professor1.getCpf())
    print(professor1.getCurso())
    print(professor1.getDisciplina())
    print(professor1.getCurso().getDisciplinas()) 
    print("===========================" * 6)

testesAluno()
testesProfessor()


# endereco = Endereco()
# endereco.setRua("Rua calango")
# endereco.setBairro("Bairro calango")
# endereco.setNumero(00)
# endereco.setCidade("Cidade calango")
# endereco.mostrarEndereco()


