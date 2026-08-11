def prestacao():
    produto = float(input("Digite o valor do produto: "))
    parcelas = float(input("Digite a quantidade de parcelas: "))
    valor_parcelas = produto / parcelas
    return produto, parcelas, valor_parcelas

produto, valor_parcelas , parcelas = prestacao()
print(f"Valor do produto: {produto}")
print(f"Quantidade de parcelas: {parcelas}")
print(f"Valor de cada parcela: {valor_parcelas}")