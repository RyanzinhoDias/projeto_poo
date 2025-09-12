class ErroSistema(Exception):
    #Classe base para todas as exceções
    pass

class ValorVazioError(ErroSistema):
    def __init__(self, campo):
        self.mensagem = f"{campo}! Tente novamente!"
        super().__init__(self.mensagem)

class ValorInvalidoError(ErroSistema):
    pass

class LivroNaoEncontradoError(ErroSistema):
    def __init__(self, identificador_livro):
        self.mensagem = f"Livro: {identificador_livro} não encontrado. Verifique se esta correto e tente novamente!"
        super().__init__(self.mensagem)

class MatriculaNaoLocalizadaError(ErroSistema):
    def __init__(self, matricula):
        self.mensagem = f"Matricula {matricula}' não foi localizada no sistema. verifique se esta correta!"
        super().__init__(self.mensagem)

class EstoqueInsuficienteError(ErroSistema):
    def __init__(self, nome_livro):
        self.mensagem = f"Não há exemplares do livro {nome_livro} disponíveis em estoque. Tente outro dia!"
        super().__init__(self.mensagem)