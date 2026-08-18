def entrega():
    compra = float(input("Digite o valor da compra: "))

    if compra <= 100:
        frete = 20
    elif compra >= 101 and compra <= 300:
        frete = 10
    else:
        frete = 0

    valor_final = compra + frete
    print(f"Valor da compra: {compra}")
    print(f"Valor da frete: {frete}")
    print(f"Valor final: {valor_final}")