from entidades.livros import lista_de_livros
from gerenciadores.gerenciador_livros import listar_livros

# listar e locar livros cadastrados
# def listar_locados():
#         contador = 0
#         for locado in lista_de_livros:
#             if locado['locado'] == True:
#                 contador += 1
#                 print(f"ID {contador}: Título: {locado['titulo']} | Autor: {locado['autor']} | Locado:Sim")
#         return contador

def locar_livro():
    listar_livros()
    while True:
        try:
            id = int(input("Digite o ID de qual cadastro de livro será locado: "))
            if lista_de_livros[id - 1]['locado'] == True:
                print("O livro não pode ser locado no momento")
            if lista_de_livros[id - 1]['locado'] == False:
                if (id > 0) and (id <= len(lista_de_livros)):
                    lista_de_livros[id - 1]['locado'] = True
                    print("Livro locado com sucesso!")
                    break
                if (id > len(lista_de_livros)) or (id <= 0):
                    print("ID inválido")
        except ValueError:
            print("ID inválido")

# devolver livros locados
# def devolver_livro():
#     contador = 0
#     for locado in lista_de_livros:
#         if locado['locado'] == True:
#             contador += 1
#             print(f"ID {contador}: Título: {locado['titulo']} | Autor: {locado['autor']} | Locado:Sim")
#     while True:
#         try:
#             id = int(input("Digite o ID de qual cadastro de livro será devolvido: "))
#             if (id > 0) and (id <= contador):
#                 lista_de_livros[contador]['locado'] = False
#                 print("Livro devolvido com sucesso!")
#                 break
#             if (id > contador) or (id <= 0):
#                 print("ID inválido")
#         except ValueError:
#             print("ID inválido")

def devolver_livro():
    listar_livros()
    while True:
        try:
            id = int(input("Digite o ID de qual cadastro de livro será devolvido: "))
            if lista_de_livros[id - 1]['locado'] == False:
                print("O livro não pode ser não está locado")
            if lista_de_livros[id - 1]['locado'] == True:
                if (id > 0) and (id <= len(lista_de_livros)):
                    lista_de_livros[id - 1]['locado'] = False
                    print("Livro devolvido com sucesso!")
                    break
                if (id > len(lista_de_livros)) or (id <= 0):
                    print("ID inválido")
        except ValueError:
            print("ID inválido")