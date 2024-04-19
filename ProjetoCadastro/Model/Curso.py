
class Curso():

    def __init__(self, nome, periodo) -> None:
        self.__nome = nome
        self.__periodo = periodo
        self.__disciplinas = [] 
        
    def _mostrarDados(self):
        print(repr)
        
    def _setNome(self, nome):
        self.__nome = nome

    def _getNome(self):
        return self.__nome
    
    def _setDisciplinas(self, disciplina):
        self.__disciplinas.extend(disciplina)

    def _getDisciplinas(self):
        return self.__disciplinas
    
    def _setPeriodo(self, periodo):
        self.__periodo = periodo
        
    def _getPeriodo(self):
        return self.__periodo
    
    def __repr__(self) -> str:
        return f"curso(s): {self.__nome}"