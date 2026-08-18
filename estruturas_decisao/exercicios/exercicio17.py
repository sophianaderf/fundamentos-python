def figura():
    lado1 = float(input("Digite o lado A do triângulo: "))
    lado2 = float(input("Digite o lado B: "))
    lado3 = float(input("Digite o lado C: "))

    if lado1 == lado2 and lado3 == lado1:
        print(f"Triângulo Equilátero")
    elif lado1 == lado2 or lado3 == lado1 or lado2 == lado3:
        print(f"Triângulo Isóceles")
    else:
        print(f"Triânguli Escaleno")

figura()