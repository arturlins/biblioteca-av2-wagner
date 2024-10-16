from entidades.livros import *
from gerenciadores.gerenciador_livros import *

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
                    editar_livro()
                    break
                case _:
                    print("Opção inválida")
                    
        except ValueError:
            print("Opção inválida")

main()