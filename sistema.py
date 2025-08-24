from excecoes import EstoqueInsuficienteError, MatriculaNaoLocalizadaError, LivroNaoEncontradoError

class Sistema:
    def __init__(self):
        self.__usuarios = list()
        self.__livros = list()
    
    def inserir_usuario(self, novo_usuario):
        self.__usuarios.append(novo_usuario)
    
    def inserir_livro(self, novo_livro):
        self.__livros.append(novo_livro)
    
    def listar_usuario(self):
        for i in self.__usuarios:
            i.impressao()

    def listar_livros(self):
        for i in self.__livros:
            i.impressao()
    
    def emprestimo(self, nome_livro, matricula):
        #buscar livro
        livro_encontrado = None
        
        for livro in self.__livros:
            if (livro.get_nome()).upper() == nome_livro.upper():
                livro_encontrado = livro
                break
        
        if livro_encontrado is None:
            raise LivroNaoEncontradoError("Livro não encontrado")
            
        
        if livro_encontrado.get_quantidade_estocada() == 0:
            raise EstoqueInsuficienteError("Não possui estoque desse livro")
        
        #busca usuario
        usuario_encontrado = None

        for usuario in self.__usuarios:
            if usuario.get_matricula() == matricula:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado is None:
            raise MatriculaNaoLocalizadaError("Matricula não localizada")
        
        #chegou aqui ta tudo ok
        usuario_encontrado.set_livros_alugados(usuario_encontrado.get_livros_alugados() + 1)
        livro_encontrado.set_quantidade_estocada(livro_encontrado.get_quantidade_estocada() - 1)
        print(f"Empréstimo realizado: {livro_encontrado.get_nome()} -> {usuario_encontrado.get_nome()}.")
        

    def devolucao(self, nome_livro, matricula):
        livro_encontrado = None
        
        for livro in self.__livros:
            if (livro.get_nome()).upper() == nome_livro.upper():
                livro_encontrado = livro
                break
        if livro_encontrado is None:
            raise LivroNaoEncontradoError("Livro não foi localizado")
        
        usuario_encontrado = None

        for usuario in self.__usuarios:
            if usuario.get_matricula() == matricula:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado is None:
            raise MatriculaNaoLocalizadaError("Matricula não localizada")

        usuario_encontrado.set_livros_alugados(usuario_encontrado.get_livros_alugados() - 1)
        livro_encontrado.set_quantidade_estocada(livro_encontrado.get_quantidade_estocada() + 1)
        print(f"Livro {livro_encontrado.get_nome()} devolvido com sucesso.")