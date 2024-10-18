from entidades.livros import lista_de_livros

# listar livros cadastrados
def listar_livros():
    for i in range (0, len(lista_de_livros)):
        print(f"ID {i + 1}: Título: {lista_de_livros[i]['titulo']} | Autor: {lista_de_livros[i]['autor']} | Locado: {'Não' if lista_de_livros[i]['locado'] == False else 'Sim'}")

# cadastrar livro
def cadastrar_livros():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    lista_de_livros.append({'titulo': titulo, 'autor': autor, 'locado': False})
    print(f'Livro cadastrado com sucesso: Título: {titulo} | Autor: {autor}')
    while True:
        try:
            opc = int(input("Deseja cadastrar outro livro:\n1 - Sim\n2 - Não\n"))
            if opc == 1:
                cadastrar_livros()
            if opc == 2:
                break
            elif opc != 1 and opc !=2:
                print("Valor inválido, digite 1 para cadastrar um novo autor ou 2 para ir para o menu principal")
        except ValueError:
            print("Valor inválido, digite 1 para cadastrar um novo autor ou 2 para ir para o menu principal")

# editar livro cadastrado
def editar_livro():
    listar_livros()
    while True:
        try:
            id = int(input("Digite o ID de qual cadastro de livro será editado: "))
            if (id > 0) and (id <= len(lista_de_livros)):
                titulo = input("Digite o título do livro: ")
                lista_de_livros[id - 1]['titulo'] = titulo
                autor = input("Digite o autor do livro: ")
                lista_de_livros[id - 1]['autor'] = autor
                print("Livro editado com sucesso")
                break
            if (id > len(lista_de_livros)) or (id <= 0):
                print("ID inválido")
        except ValueError:
            print("ID inválido")


# excluir livro cadastrado
def excluir_livro():   
    listar_livros()
    while True:
        try:
            id = int(input("Digite o ID de qual cadastro de livro será excluído: "))
            if (id > 0) and (id <= len(lista_de_livros)):
                lista_de_livros.pop(id - 1)
                print("Livro editado com sucesso")
                break
            if (id > len(lista_de_livros)) or (id <= 0):
                print("ID inválido")
        except ValueError:
            print("ID inválido")