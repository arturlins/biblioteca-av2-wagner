from entidades.usuarios import lista_de_usuarios
from os import system
import menu_principal

# Função para criar cadastro
def cadastrar_usuario():
    email = input("Digite o e-mail: ")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if email in lista_de_usuarios:
        system('cls')
        print("Usuário já cadastrado!")
        menu_principal.menu_principal()
    else:
        lista_de_usuarios.append({'email': email, 'nome': nome, 'senha': senha})
        system('cls')
        print("Usuário cadastrado com sucesso!")

# Função para fazer login
def login():
    email = input("Digite o e-mail cadastrado: ")
    senha = input("Digite a senha: ")
    validador = 0
    for usuario in lista_de_usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
           system('cls')
           print(f"Bem-vindo, {usuario['nome']}!")
           menu_principal.menu_principal()
           validador = 1
    if validador == 0:
        system('cls')
        print("Senha ou e-mail inválido.")