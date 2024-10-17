from gerenciadores.gerenciador_livros import listar_livros, cadastrar_livros

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