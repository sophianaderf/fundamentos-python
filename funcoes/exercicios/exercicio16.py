def calculoImc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)
    return peso, altura, imc

peso, altura, imc = calculoImc()
print(f"Peso em kg: {peso}")
print(f"Altura em metros: {altura}")
print(f"Valor IMC: {imc}")