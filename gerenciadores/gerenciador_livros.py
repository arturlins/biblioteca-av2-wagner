from entidades.livros import lista_de_livros

# listar livros cadastrados
def listar_livros():
    contador = 1
    for i in range (0, len(lista_de_livros)):
        print(f'ID {lista_de_livros[i]['id']}: Título: {lista_de_livros[i]['titulo']} | Autor: {lista_de_livros[i]['autor']} | Locado: {'Não' if (lista_de_livros[i]['locado'] == False) else 'Sim'}')
        contador += 1

# cadastrar livro
def cadastrar_livros():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    lista_de_livros.append([{'titulo': titulo}, {'autor': autor}, {'id': len(lista_de_livros) + 1}, {'locado': False}])
    print(f'Livro cadastrado com sucesso: Título: {titulo} | Autor: {autor}')
    listar_livros()
    # opc = input("Deseja cadastrar outro autor:\n1 - Sim\n2 - Não")
    # if input == 1:
    #     cadastrar_livros()
    # elif input == 2:
    #     main()

# editar livro cadastrado
def editar_livro():   
    print("Digite o ID de qual cadastro de livro será editado: ")
    listar_livros()
    
    while True:
        try:
            id = input(int("ID: "))
            if (id > len(lista_livros)) or (id <= 0):
                print("ID inválido")
        except ValueError:
            print("ID inválido")


# excluir livro cadastrado
def excluir_livro():   
    print("Digite o ID de qual cadastro de livro será excluído: ")
    listar_livros()