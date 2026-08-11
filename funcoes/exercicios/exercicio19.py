def energia():
    consumo_kwh =  float(input("Digite o consumo em kwh: "))
    valor_kwh = float(input(f"Digite o valor do kwh"))
    valor_conta = consumo_kwh * valor_kwh
    return consumo_kwh, valor_kwh, valor_conta

consumo_kwh, valor_kwh, valor_conta = energia()
print(f"O valor a pagar é: {valor_conta}")