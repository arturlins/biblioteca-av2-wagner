from entidades.livros import lista_de_livros
from gerenciadores.gerenciador_livros import listar_livros

# Função para locar livros previamente cadastrados
def locar_livro():
    listar_livros()
    while True:
        try:
            id = int(input("Digite o ID de qual cadastro de livro será locado: "))
            if lista_de_livros[id - 1]['locado'] == True:
                print("O livro não pode ser locado no momento")
                break
            if lista_de_livros[id - 1]['locado'] == False:
                if (id > 0) and (id <= len(lista_de_livros)):
                    lista_de_livros[id - 1]['locado'] = True
                    print("Livro locado com sucesso!")
                    break
                if (id > len(lista_de_livros)) or (id <= 0):
                    print("ID inválido")
        except ValueError:
            print("ID inválido")

# Função para devolver um livro locado
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