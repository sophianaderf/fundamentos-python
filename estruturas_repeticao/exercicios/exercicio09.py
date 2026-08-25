def contar_pares():
    inicio = int(input("Digite um número inteiro para ser o primeiro valor: "))
    fim = int(input("Digite outro número inteiro para ser o segundo valor: "))

    quantidade = 0

    for numero in range (inicio, fim + 1):
        if numero % 2 == 0:
            quantidade += 1

    return quantidade

resultado = contar_pares()

print(f"A quantidade de números pares existentes é de {resultado}")

