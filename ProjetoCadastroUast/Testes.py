import Aluno, Endereco, Professor, Curso, Disciplina, Sala


# arquivo para testes

aluno1 = Aluno.Aluno()
aluno1.setNome("jill")
aluno1.setMatricula("A001")
endereco1 = Endereco.Endereco()
endereco1.setRua("rua 1")
endereco1.setBairro("bairro dois")
endereco1.setNumero(00)
endereco1.setCidade("cidade serra talhada")
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


# print(aluno1)
# aluno1.mostrarEndereco()



professor1 = Professor.Professor()
professor1.setNome("luiz")
endereco2 = Endereco.Endereco()
endereco2.setRua("rua 3")
endereco2.setBairro("bairro seis")
endereco2.setNumero(00)
endereco2.setCidade("cidade serra talhada")
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


# endereco = Endereco.Endereco()
# endereco.setRua("Rua calango")
# endereco.setBairro("Bairro calango")
# endereco.setNumero(00)
# endereco.setCidade("Cidade calango")
# endereco.mostrarEndereco()


