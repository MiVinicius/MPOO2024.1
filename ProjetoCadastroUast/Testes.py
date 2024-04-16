import Aluno, Endereco, Professor, Curso, Disciplina, Sala


# arquivo para testes

def testesAluno():

    aluno1 = Aluno.Aluno()
    aluno1.setNome("jill")
    aluno1.setMatricula("A001")

    endereco1 = Endereco.Endereco()
    endereco1.setRua("rua 1")
    endereco1.setBairro("vila bela")
    endereco1.setNumero(110)
    endereco1.setCidade("serra talhada")
    aluno1.setEndereco(endereco1)

    curso1 = Curso.Curso()
    curso1.setNome("curso bsi")
    disciplina1 = Disciplina.Disciplina()
    disciplina1.setNome("MPOO")
    sala1 = Sala.Sala()
    sala1.setSalaNumero(12)
    sala1.setBlocoNumero(2)
    disciplina1.setSala(sala1)
    curso1.setDisciplina(disciplina1)
    aluno1.setCurso(curso1)
    aluno1.setDisciplina(disciplina1)


    print(aluno1)
    print(aluno1.mostrarEndereco())
    print(aluno1.getEndereco())
    print(aluno1.getNome())
    print(aluno1.getMatricula())
    print(aluno1.getCurso())
    print(aluno1.getDisciplina())

def testesProfessor():
    professor1 = Professor.Professor()
    professor1.setNome("luiz")
    professor1.setCpf("12345678910")

    endereco2 = Endereco.Endereco()
    endereco2.setRua("rua 3")
    endereco2.setBairro("caxixola")
    endereco2.setNumero(9)
    endereco2.setCidade("serra talhada")
    professor1.setEndereco(endereco2)

    curso2 = Curso.Curso()
    curso2.setNome("curso letras")
    disciplina2 = Disciplina.Disciplina()
    disciplina2.setNome("libras")
    sala2 = Sala.Sala()
    sala2.setSalaNumero(3)
    sala2.setBlocoNumero(1)
    disciplina2.setSala(sala2)
    curso2.setDisciplina(disciplina2)
    professor1.setCurso(curso2)
    professor1.setDisciplina(disciplina2)

    print(professor1)
    print(professor1.mostrarEndereco()) # 1 real pra quer descobrir como isso retorna None
    print(professor1.getEndereco())
    print(professor1.getNome())
    print(professor1.getCpf())
    print(professor1.getCurso())
    print(professor1.getDisciplina())


# testesAluno()
testesProfessor()


# endereco = Endereco.Endereco()
# endereco.setRua("Rua calango")
# endereco.setBairro("Bairro calango")
# endereco.setNumero(00)
# endereco.setCidade("Cidade calango")
# endereco.mostrarEndereco()


