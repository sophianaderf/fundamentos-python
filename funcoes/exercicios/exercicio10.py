def temperatura():
    graus_celsius = float(input("Digite a temperatura em graus Celsius: "))
    farenheit = graus_celsius * 1.8 + 32

    return graus_celsius, farenheit

graus_celsius, farenheit = temperatura()
print(f"Valor em Celsius: {graus_celsius}")
print(f"Valor em Farenheit: {farenheit}")