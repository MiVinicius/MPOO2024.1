
# from Aluno import Aluno
# from Professor import Professor
# from Coordenador import Coordenador
# from Diretor import Diretor


# Create
class BaseDados():
    
    alunos :list = []    # no dia que isso tiver que ficar privado, esse código já era
    servidores :list = []
    cursos :list = []
    disciplinas :list = []
    salas :list = []
    
    def inicializarBase(self):
        # aluno = Aluno("Misael", "999.999.999-99")
        # self.cadastrarAluno(aluno)
        # professor = Professor("Juliano", "124.735.846-73")
        # self.cadastrarServidor(professor)
        # coordenador = Coordenador("Gean", "034.346.786-74")
        # self.cadastrarServidor(coordenador)
        # diretor = Diretor("Mauro", "405.695.954-60")
        # self.cadastrarServidor(diretor)
        pass

    def cadastrarAluno(self, Aluno):
        BaseDados.alunos.append(Aluno)
        return True

    def cadastrarServidor(self, Servidor):
        BaseDados.servidores.append(Servidor)
        return True
    
    def cadastrarProfessor(self, Professor):
        BaseDados.servidores.append(Professor)
        return True
    
    def cadastrarCoordenador(self, Coordenador):
        BaseDados.servidores.append(Coordenador)
        return True
    
    def cadastrarDiretor(self, Diretor):
        BaseDados.servidores.append(Diretor)
        return True
    
    def cadastrarCurso(self, Curso):
        BaseDados.cursos.append(Curso)
        return True
    
    def cadastrarDisciplina(self, Disciplina):
        BaseDados.disciplinas.append(Disciplina)
        return True
    
    def cadastrarSala(self, Sala):
        BaseDados.salas.append(Sala)
        return True
    
    def buscarAluno(self, aluno_procurado):
        for aluno_atual in BaseDados.alunos:
            if aluno_atual._getNome() == aluno_procurado._getNome():
                if aluno_atual._getCpf() == aluno_procurado._getCpf():
                    return aluno_atual
        return None
    
    def buscarServidor(self, servidor_procurado):
        for servidor_atual in BaseDados.servidores:
            if  servidor_atual._getNome()==servidor_procurado._getNome():
                if servidor_atual._getCpf() == servidor_procurado._getCpf():
                    return servidor_atual
        return None

    def buscarCurso(self, id_curso):
        for curso in BaseDados.cursos:
            if curso._getNome() == id_curso._getNome():
                return curso
    
    def buscarDisciplina(self, id_disciplina):
        for disciplina in BaseDados.disciplinas:
            if disciplina._getNome() == id_disciplina:
                return disciplina
    
    def buscarSala(self, id_sala):
        for sala in BaseDados.salas:
            if sala._getNome() == id_sala._getNome():
                if sala._getBloco() == id_sala._getBloco():
                    return sala
        return None
    
    def atualizarAluno(self, id_aluno, novos_dados):
        for aluno in BaseDados.alunos:
            if aluno._getNome() == id_aluno._getNome():
                if aluno._getCpf() == id_aluno._getCpf():
                    BaseDados.alunos.index(aluno)._setNome(novos_dados._getNome())
                    BaseDados.alunos.index(aluno)._setCpf(novos_dados._getCpf())
                    BaseDados.alunos.index(aluno)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    def atualizarServidor(self, id_pessoa, novos_dados):
        for servidor in BaseDados.servidores:
            if servidor._getNome() == id_pessoa._getNome():
                if servidor._getCpf() == id_pessoa._getCpf():
                    BaseDados.servidores.index(servidor)._setNome(novos_dados._getNome())
                    BaseDados.servidores.index(servidor)._setCpf(novos_dados._getCpf())
                    BaseDados.servidores.index(servidor)._setEndereco(novos_dados._getEndereco())
                    return True
        return False
    
    def atualizarCurso(self, id_curso, novos_dados):
        for curso in BaseDados.cursos:
            if curso._getNome() == id_curso._getNome():
                BaseDados.cursos.index(curso)._setNome(novos_dados._getNome()) 
                BaseDados.cursos.index(curso)._setPeriodo(novos_dados._getPeriodo())
                BaseDados.cursos.index(curso)._setCoordenador(novos_dados._getCoordenador())
                return True
        return False
    
    def atualizarDisciplina(self, id_disciplina, novos_dados): 
        for disciplina in BaseDados.disciplinas:
            if disciplina._getNome() == id_disciplina._getNome():
                BaseDados.disciplinas.index(disciplina)._setNome(novos_dados._getNome())
                return True
        return False
    
    def atualizarSala(self, id_sala, novos_dados):
        for sala in BaseDados.salas:
            if sala._getSalaNumero() == id_sala._getSalaNumero() and sala._getBlocoNumero() == id_sala._getBlocoNumero():
                BaseDados.salas.index(sala)._setNome(novos_dados._getNome()), BaseDados.salas.index(sala)._setBloco(novos_dados._getBloco())
                return True
        return False
    
    def deletarAluno(self, Aluno):
        BaseDados.alunos.remove(Aluno)
        return True
    
    def deletarServidor(self, Servidor):
        BaseDados.servidores.remove(Servidor)
        return True
    
    def deletarCurso(self, Curso):
        Curso._setDisciplinas(None) 
        BaseDados.cursos.remove(Curso)  
        return True
    
    def deletarDisciplina(self, Disciplina):
        BaseDados.disciplinas.remove(Disciplina)
        return True
    
    def deletarSala(self, Sala):
        return BaseDados.salas.remove(Sala)
    
    def deletarBase(self):      
        BaseDados.alunos.clear()
        BaseDados.servidores.clear()
        print("Base Deletada com Sucesso!")
    
    def listarAlunos(self):
        print("Lista dos alunos:")
        for aluno in BaseDados.alunos:
            print(aluno._getNome(), aluno._getCpf(), aluno._getMatricula(), aluno._getEndereco(), aluno._getCurso(), aluno._getDisciplina()) 
    
    def listarServidores(self):
        print("Lista dos servidores:")
        for servidor in BaseDados.servidores:
            print(servidor._getNome(), servidor._getCpf(), servidor._getEndereco(), servidor._getSala())
    
    def listarCursos(self):
        print("Lista dos Cursos:")
        for curso in BaseDados.cursos:
            print(curso.getNome(), curso.getPeriodo())
            print(curso.getDisciplinas())
            print(curso.getSalas())
    
    def listarDisciplinas(self):
        print("Lista das Disciplinas:")
        for disciplina in BaseDados.disciplinas:
            print(disciplina.getNome(), disciplina.getSala())
    
    def listarSalas(self):
        print("Lista das Salas:")
        for sala in BaseDados.salas:
            print(sala.getNumero(), sala.getBloco())
    
