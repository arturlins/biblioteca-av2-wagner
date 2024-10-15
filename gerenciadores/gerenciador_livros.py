from entidades.livros import lista_livros

# listar livros cadastrados
def listar_livros():
    for livro in lista_livros():
        print(f'ID {livro['id']}: {livro['titulo']}, de {livro['autor']}')

# cadastrar livro

# editar livro cadastrado
def editar_livro():   
    print("Digite o ID de qual cadastro de livro será editado: ")
    listar_livros()


# excluir livro cadastrado