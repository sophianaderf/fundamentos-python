def ingresso():
    idade = int(input("Digite sua idade:"))
    if idade <= 5:
        print("Valor do ingresso: gratuito")
    elif idade >= 6 and idade <= 12:
        print("Valor do ingresso: R$ 10,00")
    elif idade >= 13 and idade <= 59:
        print("Valor do ingresso: R$ 20,00")
    else:
        print("Valor do ingresso: R$ 10,00")

ingresso()