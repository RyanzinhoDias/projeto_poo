class ValorVazioError(Exception):
    """Exceção para quando um campo está vazio."""
    pass

class ValorInvalidoError(Exception):
    """Exceção para quando um valor é inválido."""
    pass

class LivroNaoEncontradoError(Exception):
    """Exceção para quando um livro não é encontrado."""
    pass

class MatriculaNaoLocalizadaError(Exception):
    """Exceção para quando a matrícula do usuário não é encontrada."""
    pass

class EstoqueInsuficienteError(Exception):
    """Exceção para quando não há estoque disponível."""
    pass