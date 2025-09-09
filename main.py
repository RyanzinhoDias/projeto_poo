from sistema import Sistema
from usuario import Usuario
from livros import Livros
from excecoes import ErroSistema

def exibir_menu():
    print("\n======= SISTEMA DE BIBLIOTECA =======")
    print("|  [1] - Cadastrar novo usuário       |")
    print("|  [2] - Cadastrar Livro              |")
    print("|  [3] - Realizar empréstimo de Livro |")
    print("|  [4] - Realizar devolução de Livro  |")
    print("|  [5] - Listar todos os usuários     |")
    print("|  [6] - Listar todos os Livros       |")
    print("|  [7] - Sair do Sistema              |")
    print("=======================================")

def carregar_dados_iniciais(sistema):
    #Apenas para os sistemas já ter dados cadastrados
    u1 = Usuario("Ana", "202301", "Engenharia")
    u2 = Usuario("Beto", "202302", "Computação")
    l1 = Livros("O Senhor dos Anéis", "Fantasia", "J.R.R. Tolkien", 3)
    l2 = Livros("1984", "Distopia", "George Orwell", 0)
    try:
        sistema.inserir_usuario(u1)
        sistema.inserir_usuario(u2)

        sistema.inserir_livro(l1)
        sistema.inserir_livro(l2)
        print(">>> Dados iniciais carregados com sucesso! <<<")
    except ErroSistema as e:
        print(f"Ocorreu um erro ao carregar dados iniciais: {e}")

def cadastrar_usuario(sistema):
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome do usuário: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    try:
        
        novo_usuario = Usuario(nome, matricula, curso)
        sistema.inserir_usuario(novo_usuario)
        print(">>> Usuário cadastrado com sucesso! <<<")
    except ErroSistema as e:
        print(f"!!! Erro no cadastro: {e} !!!")

def cadastrar_livro(sistema):
    print("\n--- Cadastro de Livro ---")
    nome = input("Nome do livro: ")
    genero = input("Gênero: ")
    autor = input("Autor: ")
    try:
        pare = 0
        while pare != 1:
            quantidade = int(input("Quantidade em estoque: "))
            try:
                pare = 1
            except ValueError:
                print("!!! Quantidade inválida. Por favor, digite um número inteiro. !!!")
        
        novo_livro = Livros(nome, genero, autor, quantidade)
        sistema.inserir_livro(novo_livro)
        print(">>> Livro cadastrado com sucesso! <<<")
    except ErroSistema as e:
        print(f"!!! Erro no cadastro: {e} !!!")

def realizar_emprestimo(sistema):
    print("\n--- Empréstimo de Livro ---")
    nome_livro = input("Digite o nome do livro: ")
    matricula_usuario = input("Digite a matrícula do usuário: ")
    try:
        sistema.emprestimo(nome_livro, matricula_usuario)
    except ErroSistema as e:
        print(f"!!! Erro ao realizar empréstimo: {e} !!!")

def realizar_devolucao(sistema):
    print("\n--- Devolução de Livro ---")
    nome_livro = input("Digite o nome do livro: ")
    matricula_usuario = input("Digite a matrícula do usuário: ")
    try:
        sistema.devolucao(nome_livro, matricula_usuario)
    except ErroSistema as e:
        print(f"!!! Erro ao realizar devolução: {e} !!!")
#Principal
def main():
    sistema_biblioteca = Sistema()
    carregar_dados_iniciais(sistema_biblioteca)
    opcao = 0
    while opcao != '7':
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            cadastrar_usuario(sistema_biblioteca)
        elif opcao == '2':
            cadastrar_livro(sistema_biblioteca)
        elif opcao == '3':
            realizar_emprestimo(sistema_biblioteca)
        elif opcao == '4':
            realizar_devolucao(sistema_biblioteca)
        elif opcao == '5':
            print("\n-- Lista de Usuários --")
            sistema_biblioteca.listar_usuario()
        elif opcao == '6':
            print("\n-- Lista de Livros --")
            sistema_biblioteca.listar_livros()
        elif opcao == '7':
            print("Encerrando o sistema. Até mais!")
        else:
            print("!!! Opção inválida. Por favor, escolha uma opção do menu. !!!")

if __name__ == "__main__":
    main()