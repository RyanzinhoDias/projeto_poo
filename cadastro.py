from excecoes import ValorVazioError

class Cadastro:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome):
        if not novo_nome:
            raise ValorVazioError("O nome não pode ser vazio") 
        self.__nome = novo_nome

    def impressao(self):
        print("Nome: ", self.get_nome())
        