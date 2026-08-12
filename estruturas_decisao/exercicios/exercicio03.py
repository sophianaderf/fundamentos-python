def valor():
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print(f"Você possui {idade} anos, sendo assim, maior de idade.")
    else:
        print(f"Você possui {idade} anos, sendo assim, menor de idade.")
    return idade

valor()