def jogo_adivinhacao():
    numero_secreto = 8

    while True:
        palpite = int(input("Digite um número: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite > numero_secreto:
            print("O palpite é maior que o número secreto!")
        else:
            print("O palpite é menor que o número secreto!")


jogo_adivinhacao()