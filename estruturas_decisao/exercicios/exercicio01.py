def valor():
    numero = int(input("Digite um numero inteiro: "))


    if numero > 0:
        print(f"{numero} é um número positivo")

    elif numero < 0:
        print(f"{numero} é um numero negativo")

    else:
        print(f"{numero} é nulo")

    return numero
valor()