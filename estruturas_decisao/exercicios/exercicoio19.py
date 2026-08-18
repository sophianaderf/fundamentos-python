def classificacao():
    numero = int(input("Digite um numero inteiro: "))

    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    if numero % 2 == 0:
        classificacao = "par"
    else:
        classificacao = "impar"

    print(f"Número: {numero}")
    print(f"Número {sinal} e {classificacao}")

classificacao()
