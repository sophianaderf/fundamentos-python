def somar_pares():
    inicio = int(input("Digite um número inteiro para ser o primeiro valor: "))
    fim = int(input("Digite outro número inteiro para ser o segundo valor: "))

    soma = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            soma += numero

    return soma

resultado = somar_pares()

print(f"A soma dos números pares existentes é de {resultado}")
