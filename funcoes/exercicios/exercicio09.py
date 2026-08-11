def valor():
    valor_metros = float(input("Digite um valor em metros: "))
    valor_centimetros = valor_metros * 100


    return valor_metros, valor_centimetros


valor_metros, valor_centimetros = valor()

print(f"Valor em metros: {valor_metros}")
print(f"Conversão para centímetros: {valor_centimetros}")

