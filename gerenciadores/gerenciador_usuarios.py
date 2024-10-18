from entidades.usuarios import lista_de_usuarios   
import menu_pos_login

# criar cadastro
def cadastrar_usuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in lista_de_usuarios:
        print("Usuário já cadastrado!")
    else:
        lista_de_usuarios[usuario] = senha  
        print("Usuário cadastrado com sucesso!")
# fazer login
def login():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in lista_de_usuarios and lista_de_usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
        menu_pos_login()
    else:
        print("Usuário ou senha incorretos!")
