from gerenciadores.gerenciador_livros import listar_livros, cadastrar_livros, editar_livro, excluir_livro
from gerenciadores.gerenciador_locacao import locar_livro, devolver_livro

def menu_principal():

    while True:
        try:
            print("Bem-vindo ao Sistema de Biblioteca do CESMAC\nEscolha uma opção abaixo: ")
            print("1 - listar os livros cadastrados")
            print("2 - cadastrar novos livros")
            print("3 - editar o cadastro de um livro")
            print("4 - excluir o cadastro de um livro")
            print("5 - locar um livro")
            print("6 - devolver um livro")
            print("7 - Sair do sistema")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    listar_livros()
                case 2:
                    cadastrar_livros()
                case 3:
                    editar_livro()
                case 4:
                    excluir_livro()
                case 5:
                    locar_livro()
                case 6:
                    devolver_livro()
                case 7:
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida")
                    
        except ValueError:
            print("Opção inválida")