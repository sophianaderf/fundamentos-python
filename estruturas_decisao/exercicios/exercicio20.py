def caixa():
    saldo = float(input("Qual o valor do saldo disponível: "))
    saque = float(input("Qual o valor do saque: "))

    if saque <= 0:
        print("Valor do saque inválido")
    elif saque > saldo:
        print(f"Saldo negativo")
    else:
        novosaldo = saldo - saque
        print(f"Saque realizado com sucesso")
        print(f"Novo saldo: {novosaldo}")
caixa()