from cadastro import Cadastro
from excecoes import ValorInvalidoError, ValorVazioError

class Usuario(Cadastro):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome)
        self.__matricula = matricula
        self.__curso = curso
        self.__livros_alugados = 0
    
    def get_matricula(self):
        return self.__matricula
    def get_curso(self):
        return self.__curso
    def get_livros_alugados(self):
        return self.__livros_alugados

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
    def set_curso(self, novo_curso):
        self.__curso = novo_curso
    def set_livros_alugados(self, quantidade):
        self.__livros_alugados = quantidade
    
    def impressao(self):
        print("--- Usuário ---")
        super().impressao()
        print("Matricula: ", self.get_matricula())
        print("Curso: ", self.get_curso())
        print("Qtd livros alugados: ", self.get_livros_alugados())