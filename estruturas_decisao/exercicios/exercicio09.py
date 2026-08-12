def calculo():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha uma operação (+, -, * ou /): ")

    if operacao == "+":
        adicao = numero1 + numero2
        print("Operação escolhida: Adição")
        print(f"Resultado: {adicao}")

    elif operacao == "-":
        subtracao = numero1 - numero2
        print("Operação escolhida: Subtração")
        print(f"Resultado: {subtracao}")

    elif operacao == "*":
        multiplicacao = numero1 * numero2
        print("Operação escolhida: Multiplicação")
        print(f"Resultado: {multiplicacao}")

    elif operacao == "/":
        if numero2 != 0:
            divisao = numero1 / numero2
            print("Operação escolhida: Divisão")
            print(f"Resultado: {divisao}")
        else:
            print("Não é possível realizar a divisão.")

    else:
        print("Operação inválida!")

calculo()