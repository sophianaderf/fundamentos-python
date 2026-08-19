def tabuada():
    numero = int(input("Digite um número inteiro: "))

    for i in range(1, 11):
        conta = numero * i
        print(f"{numero} x {i} = {conta}")
tabuada()