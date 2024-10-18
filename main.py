from gerenciadores.gerenciador_usuarios import cadastrar_usuario, login
from menu_principal import menu_principal

def main():
    print("Bem-vindo ao Sistema de Biblioteca do CESMAC\nEscolha uma opção abaixo: ")
    while True:
        try:            
            print("1 - Criar cadastro")
            print("2 - Fazer login")
            print("3 - Sair do sistema")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    cadastrar_usuario()
                case 2:
                    login()
                case 3:
                    print("Saindo...")
                    break
                case 4:
                    menu_principal()
                case _:
                    print("Opção inválida")          
        except ValueError:
            print("Opção inválida")

main()