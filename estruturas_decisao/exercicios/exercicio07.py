def calor():
    temperatura = float(input("Qual a temperatura em graus Celsius: "))
    if temperatura <= 15:
        print(f"Temperatura: {temperatura}")
        print("Frio")
    elif temperatura >= 15 and temperatura <= 25:
        print(f"Temperatura: {temperatura}")
        print("Agradável")
    else:
        print(f"Temperatura: {temperatura}")
        print("Quente")
    return temperatura
calor()