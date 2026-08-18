def compra():
    valor = float(input("Qual o valor do produto? "))

    if valor <= 100:
        desconto = 0
        valor_final = valor

        print(f"Valor do produto: R$ {valor}")
        print("Desconto: 0%")
        print(f"Valor final da compra: R$ {valor_final}")

    elif valor <= 500:
        desconto = valor * 0.10
        valor_final = valor - desconto

        print(f"Valor do produto: R$ {valor}")
        print("Desconto: 10%")
        print(f"Valor final da compra: R$ {valor_final}")

    else:
        desconto = valor * 0.15
        valor_final = valor - desconto

        print(f"Valor do produto: R$ {valor}")
        print("Desconto: 15%")
        print(f"Valor final da compra: R$ {valor_final}")


compra()