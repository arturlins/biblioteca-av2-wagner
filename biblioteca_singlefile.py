# lista livros
lista_de_livros = [
    {'titulo': 'Vidas Secas', 'autor': 'Graciliano Ramos', 'id': 1, 'locado': False},
    {'titulo': 'A Hora da Estrela', 'autor': 'Clarice Lispector', 'id': 2, 'locado': False},
    {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'id': 3, 'locado': False},
    {'titulo': 'Grande Sertão: Veredas', 'autor': 'João Guimarães Rosa', 'id': 4, 'locado': False},
    {'titulo': 'Feliz Ano Novo', 'autor': 'Rubem Fonseca', 'id': 5, 'locado': False}
]

# lista usuários
def lista_usuarios():
    usuario = [
        {'nome': 'João da Silva Santos', 'email': 'joaosilva@cesmac.edu.br', 'senha': '1234', 'id': 1},
        {'nome': 'Ana Bispo da Cunha', 'email': 'anacunha@cesmac.edu.br', 'senha': 'cesmac', 'id': 2},
        {'nome': 'Maria Pereira Costa', 'email': 'mariacosta@cesmac.edu.br', 'senha': 'maria', 'id': 3},
        {'nome': 'Ivo José Bulhões','email': 'ivobulhoes@cesmac.edu.br', 'senha': 'flamengo', 'id': 4}
    ]
    return usuario

# listar livros cadastrados
def listar_livros():
    contador = 1
    for i in range (0, len(lista_de_livros)):
        print(f'ID {lista_de_livros[i]['id']}: Título: {lista_de_livros[i]['titulo']} | Autor: {lista_de_livros[i]['autor']} | Locado: {'Não' if lista_de_livros[i]['locado'] == False else 'Sim'}')
        contador += 1

# editar livro cadastrado
def editar_livro():   
    print("Digite o ID de qual cadastro de livro será editado: ")
    listar_livros()
    id = input(int("ID: "))
    while True:
        try:
            if (id > len(lista_de_livros)) or (id <= 0):
                print("ID inválido")
        except ValueError:
            print("ID inválido")

# cadastrar livro
def cadastrar_livros():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    lista_de_livros.append([{'titulo': titulo}, {'autor': autor}, {'id': len(lista_de_livros) + 1}, {'locado': False}])
    print(f'Livro cadastrado com sucesso: Título: {titulo} | Autor: {autor}')
    main()

def main():
    print("Bem-vindo ao Sistema de Biblioteca do CESMAC\nEscolha uma opção abaixo: ")
    print("Digite 1 para listar os livros")
    while True:
        try:
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    listar_livros()
                    break
                case 2:
                    cadastrar_livros()
                    break
                case _:
                    print("Opção inválida")
                    
        except ValueError:
            print("Opção inválida")

main()


# def main():
#     while True:
#         print("Bem-vindo ao Sistema de Biblioteca do CESMAC\nEscolha uma opção abaixo: ")
#         print("Digite 1 para listar os livros")
#         try:
#             opc = int(input("Selecione a opção: "))
#             if (opc == 1):
#                 listar_livros()
#                 break
#             if (opc == 2):
#                 editar_livro()
#                 break
#         except ValueError:
#             print("Caracter inválido")

# main()