def compra():
    valor = float(input("Digite o valor do produto: "))
    desconto_percentual = float(input("Digite o percentual de desconto do produto: "))
    desconto_decimal = desconto_percentual / 100
    fator_desconto =  1 - desconto_decimal
    valor_total = valor * fator_desconto
    return valor, desconto_percentual, desconto_decimal, fator_desconto, valor_total

valor, desconto_percentual, desconto_decimal, fator_desconto, valor_total = compra()
print(f"Valor do produto: {valor}")
print(f"Percentual do desconto: {desconto_percentual}")
print(f"Valor final do produto: {valor_total}")

