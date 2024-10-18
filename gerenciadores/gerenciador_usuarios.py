from entidades.usuarios import lista_de_usuarios   
import menu_principal

# criar cadastro
def cadastrar_usuario():
    email = input("Digite o e-mail: ")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if email in lista_de_usuarios:
        print("Usuário já cadastrado!")
        menu_principal.menu_principal()
    else:
        lista_de_usuarios.append({'email': email, 'nome': nome, 'senha': senha})
        print("Usuário cadastrado com sucesso!")
        print(lista_de_usuarios)

# fazer login
def login():
    email = input("Digite o e-mail cadastrado: ")
    senha = input("Digite a senha: ")
    for usuario in lista_de_usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
           print(f"Bem-vindo, {usuario['nome']}!")
           menu_principal.menu_principal()
        else:
            print("Senha ou e-mail inválido.")


print
