from entidades.livros import lista_de_livros
from gerenciadores.gerenciador_livros import listar_livros
from os import system

# Função para locar livros previamente cadastrados
def locar_livro():
    listar_livros()
    while True:
        try:
            id = int(input("Digite o ID de qual cadastro de livro será locado: "))
            if id <= 0 or id > len(lista_de_livros):
                system('cls')
                listar_livros()
                print("ID inválido")
            elif lista_de_livros[id - 1]['locado'] == True:
                system('cls')
                print("O livro não pode ser locado no momento")
                break
            else:
                lista_de_livros[id - 1]['locado'] = True
                system('cls')
                print("Livro locado com sucesso!")
                break
        except ValueError:
            system('cls')
            listar_livros()
            print("ID inválido")

# Função para devolver um livro locado
def devolver_livro():
    listar_livros()
    while True:
        try:
            id = int(input("Digite o ID de qual cadastro de livro será devolvido: "))
            if id <= 0 or id > len(lista_de_livros):
                system('cls')
                listar_livros()
                print("ID inválido")
            elif lista_de_livros[id - 1]['locado'] == False:
                print("O livro não está locado")
            else:
                lista_de_livros[id - 1]['locado'] = False
                system('cls')
                print("Livro devolvido com sucesso!")
                break
        except ValueError:
            system('cls')
            listar_livros()
            print("ID inválido")