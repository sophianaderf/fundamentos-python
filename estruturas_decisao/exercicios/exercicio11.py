def calculo():
    altura = float(input("Digite  sua altura em metros: "))
    peso = float(input("Digite o seu peso em kg: "))
    imc = peso / (altura * altura)

    print(f"IMC: {imc}")
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")

calculo()