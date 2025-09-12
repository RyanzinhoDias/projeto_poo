import unittest
from sistema import Sistema
from usuario import Usuario
from livros import Livros
from excecoes import ValorInvalidoError, EstoqueInsuficienteError, ValorVazioError, LivroNaoEncontradoError

class TestSistemaBiblioteca(unittest.TestCase):

    def setUp(self):
        self.sistema = Sistema()
        self.livro1 = Livros("Livro A", "Gênero X", "Autor Y", 1)
        self.usuario1 = Usuario("Usuário Teste", "mat01", "Curso Z")
        self.sistema.inserir_livro(self.livro1)
        self.sistema.inserir_usuario(self.usuario1)

    def test_emprestimo_sucesso(self):
        self.sistema.emprestimo("Livro A", "mat01")
        
        self.assertEqual(self.livro1.get_quantidade_estocada(), 0, "O estoque do livro deveria ser 0 após o empréstimo.")
        self.assertEqual(self.usuario1.get_livros_alugados(), 1, "O usuário deveria ter 1 livro alugado.")

    def test_devolucao_sucesso(self):
        self.sistema.emprestimo("Livro A", "mat01")

        self.sistema.devolucao("Livro A", "mat01")
        
        self.assertEqual(self.livro1.get_quantidade_estocada(), 1, "O estoque do livro deveria voltar a ser 1.")
        self.assertEqual(self.usuario1.get_livros_alugados(), 0, "O usuário deveria ter 0 livros alugados.")


    def test_emprestimo_livro_inexistente(self):
        with self.assertRaises(LivroNaoEncontradoError):
            self.sistema.emprestimo("Livro Inexistente", "mat01")

    def test_emprestimo_livro_sem_estoque(self):
        
        self.sistema.emprestimo("Livro A", "mat01")
        
        with self.assertRaises(EstoqueInsuficienteError):
            self.sistema.emprestimo("Livro A", "mat01")

    def test_criar_usuario_com_nome_vazio(self):

        with self.assertRaises(ValorVazioError):
            Usuario("", "mat02", "Curso B")

if __name__ == '__main__':
    unittest.main(verbosity=2)