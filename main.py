from entidades.livros import *
from gerenciadores.gerenciador_livros import *

def main():
    while True:
        print("Bem-vindo ao Sistema de Biblioteca do CESMAC\nEscolha uma opção abaixo: ")
        print("Digite 1 para listar os livros")
        try:
            opc = int(input("Selecione a opção: "))
            if (opc == 1):
                listar_livros()
            if (opc == 2):
                break
        except ValueError:
            print("Caracter inválido")

main()