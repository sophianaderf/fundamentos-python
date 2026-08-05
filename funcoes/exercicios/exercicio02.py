def nome():
    nome_usuario = input("Olá, qual o seu nome? ")
    return nome


def idade():
    idade = int(input("Qual a sua idade? "))
    return idade

nome_usuario = nome()
idade_usuario = idade()


print(f"{nome_usuario} possui {idade_usuario} anos")
