def impares():
    numero = int(input("Digite um número inteiro: "))

    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(f"Números ímpares: {i}")

impares()