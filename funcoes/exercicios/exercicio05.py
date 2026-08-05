def numero():
    numero_escolhido = float(input("Qual número deseja consultar? "))

    antecessor = numero_escolhido - 1
    sucessor = numero_escolhido + 1

    return numero_escolhido, antecessor, sucessor


numero_escolhido, antecessor, sucessor = numero()

print(f"Número: {numero_escolhido}\n")
print(f"Antecessor: {antecessor}\n")
print(f"Sucessor: {sucessor}")