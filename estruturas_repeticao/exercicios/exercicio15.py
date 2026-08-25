def maior_numero():
    maior = 0

    while True:
        numero = int(input("Digite um número: "))

        if numero > maior:
            maior = numero

        continuar = input("Deseja continuar? (s/n): ")

        if continuar == "n":
            break

    return maior


resultado = maior_numero()

print(f"O maior número informado foi: {resultado}")