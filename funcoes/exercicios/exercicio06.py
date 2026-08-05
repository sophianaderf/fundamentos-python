def numero():
    numero_escolhido = float(input("Qual número deseja consultar? "))

    dobro = numero_escolhido * 2
    triplo = numero_escolhido * 3

    return numero_escolhido, dobro, triplo


numero_escolhido, dobro, triplo = numero()

print(f"Número: {numero_escolhido}\n")
print(f"Dobro: {dobro}\n")
print(f"Triplo: {triplo}")