def figura():
    base = float(input("Digite o valor correspondente a base da figura: "))
    altura = float(input("Digite o valor da altura da figura: "))

    area = base * altura
    perimetro = 2 * (base + altura)

    return base, altura, area, perimetro


base, altura, area, perimetro = figura()
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

