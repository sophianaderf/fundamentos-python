def compra():
    valor = float(input("Qual o valor do produto?"))
    if valor <= 100:
        print("Desconto = 0")
        print(f"Valor final da compra: {valor}")
    elif valor <= 200:

