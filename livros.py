from cadastro import Cadastro
from random import randint
from excecoes import ValorInvalidoError, ValorVazioError

class Livros(Cadastro):
    def __init__(self, nome, genero, autor, quantidade_estocada):
        super().__init__(nome)
        self.__inscricao = self.__numero_inscricao()
        self.set_genero(genero)
        self.set_autor(autor)
        self.set_quantidade_estocada(quantidade_estocada)

    def __numero_inscricao(self):
        return randint(1000, 9999)
        
    def get_genero(self):
        return self.__genero
    def get_autor(self):
        return self.__autor
    def get_numero_incricao(self):
        return self.__numero_inscricao
    def get_quantidade_estocada(self):
        return self.__quantidade_estocada

    def set_genero(self, novo_genero):
        if not novo_genero:
            raise ValorVazioError("Genero não pode ser vazio")
        self.__genero = novo_genero

    def set_autor(self, novo_autor):
        if not novo_autor:
            raise ValorVazioError("Nome do autor não pode ser vazio")
        self.__autor = novo_autor

    def set_quantidade_estocada(self, nova_qtd):
        if not isinstance(nova_qtd, int) or nova_qtd < 0:
            raise ValorInvalidoError("A quantidade estocada deve ser um número inteiro positivo.")
        self.__quantidade_estocada = nova_qtd
    
    def impressao(self):
        print("--- LIVRO ---")
        super().impressao()
        print("Numero de inscrição: ", self.__inscricao)
        print("Genero: ", self.get_genero())
        print("Autor: ", self.get_autor())
        print("Quantidade Estocada: ", self.get_quantidade_estocada())
