class ErroSistema(Exception):
    """ Classe base para todas as exceções do sistema, captura todos os erros da class
    de forma genérica"""
    pass

class ValorVazioError(ErroSistema):
    """Exceção para quando um campo está vazio."""
    def __init__(self, campo):
        self.mensagem = f"O campo '{campo}' não pode ser vazio!, Tente novamente!"
        super().__init__(self.mensagem)
    

class ValorInvalidoError(ErroSistema):
    """Exceção para quando um valor é inválido."""
    pass

class LivroNaoEncontradoError(ErroSistema):
    """Exceção para quando um livro não é encontrado no sistema."""
    def __init__(self, identificador_livro):
        self.mensagem = f"O Livro com o identificador '{identificador_livro}' não foi encontrado!. Verifique se esta correto e tente novamente!"
        super().__init__(self.mensagem)

class MatriculaNaoLocalizadaError(ErroSistema):
    """Exceção para quando a matrícula do usuário não é encontrada."""
    def __init__(self, matricula):
        self.mensagem = f"A matricula digitada: '{matricula}' não foi localizada no sistema. verifique se esta correta!"
        super().__init__(self.mensagem)

class EstoqueInsuficienteError(ErroSistema):
    """Exceção para quando não há estoque disponível."""
    def __init__(self, nome_livro):
        self.mensagem = f"Não há exemplares do livro {nome_livro} disponíveis em estoque. Tente outro dia!"
        super().__init__(self, nome_livro)