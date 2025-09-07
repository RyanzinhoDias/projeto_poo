"""Classe criada apenas para realizar Testes"""

import unittest
from sistema import Sistema
from usuario import Usuario
from livros import Livros
from excecoes import ValorInvalidoError, EstoqueInsuficienteError, ValorVazioError, LivroNaoEncontradoError

class TestSistemaBiblioteca(unittest.TestCase):

    def setUp(self):
        """
        Este método é executado antes de cada teste.
        Cria um ambiente limpo e isolado para cada cenário de teste.
        """
        self.sistema = Sistema()
        self.livro1 = Livros("Livro A", "Gênero X", "Autor Y", 1)
        self.usuario1 = Usuario("Usuário Teste", "mat01", "Curso Z")
        self.sistema.inserir_livro(self.livro1)
        self.sistema.inserir_usuario(self.usuario1)

    # --- Testes Positivos (Caminho Feliz) ---

    def test_emprestimo_sucesso(self):
        """
        [Teste Positivo] Testa se um empréstimo válido funciona como esperado,
        alterando o estoque e a quantidade de livros do usuário.
        """
        # Ação
        self.sistema.emprestimo("Livro A", "mat01")
        
        # Verificação
        self.assertEqual(self.livro1.get_quantidade_estocada(), 0, "O estoque do livro deveria ser 0 após o empréstimo.")
        self.assertEqual(self.usuario1.get_livros_alugados(), 1, "O usuário deveria ter 1 livro alugado.")

    def test_devolucao_sucesso(self):
        """
        [Teste Positivo] Testa se uma devolução válida reverte o estado
        do empréstimo corretamente.
        """
        # Cenário inicial: é preciso emprestar antes de devolver
        self.sistema.emprestimo("Livro A", "mat01")
        
        # Ação
        self.sistema.devolucao("Livro A", "mat01")
        
        # Verificação
        self.assertEqual(self.livro1.get_quantidade_estocada(), 1, "O estoque do livro deveria voltar a ser 1.")
        self.assertEqual(self.usuario1.get_livros_alugados(), 0, "O usuário deveria ter 0 livros alugados.")

    # --- Testes Negativos (Casos de Falha Esperada) ---

    def test_emprestimo_livro_inexistente(self):
        """
        [Teste Negativo] Testa se o sistema levanta um erro correto ao tentar
        emprestar um livro que não existe no acervo.
        """
        # Ação e Verificação juntas
        # Esperamos que o bloco de código levante a exceção LivroNaoEncontradoError
        with self.assertRaises(LivroNaoEncontradoError):
            self.sistema.emprestimo("Livro Inexistente", "mat01")

    def test_emprestimo_livro_sem_estoque(self):
        """
        [Teste Negativo] Testa a tentativa de empréstimo de um livro com estoque zero.
        """
        # Esgota o estoque do livro
        self.sistema.emprestimo("Livro A", "mat01")
        
        # Ação e Verificação
        # Agora, ao tentar emprestar de novo, esperamos um erro de estoque
        with self.assertRaises(EstoqueInsuficienteError):
            self.sistema.emprestimo("Livro A", "mat01")

    def test_criar_usuario_com_nome_vazio(self):
        """
        [Teste Negativo] Testa se a criação de um objeto Usuario com nome
        vazio levanta a exceção correta.
        """
        # Ação e Verificação
        with self.assertRaises(ValorVazioError):
            Usuario("", "mat02", "Curso B")


# Permite que o arquivo seja executado diretamente
if __name__ == '__main__':
    unittest.main(verbosity=2)