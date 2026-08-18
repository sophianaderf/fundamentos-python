def login():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if senha == "1234" :
        print("Usuário não encontrado")
    elif  nome == "admin":
        print("Senha incorreta")
    else:
        print("Login realizado com sucesso")