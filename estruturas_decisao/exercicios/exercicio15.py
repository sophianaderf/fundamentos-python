def multa():
    velocidade = int(input("Digite a velocidade:"))

    if velocidade <= 60:
        print("Velocidade permitida")

    elif velocidade >= 61 and velocidade <= 80:
        print("Atenção: Velocidade acima do permitido")
    else:
        print("Multa por excsso de velocidade")

multa()