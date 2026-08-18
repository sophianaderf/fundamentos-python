def eleicao():
    idade = int(input("Digite sua idade:"))

    if idade <= 16:
        print("Não pode votar")
    if idade >= 16 and idade <= 17:
        print("Voto opcional")
    if idade >= 18 and idade <= 69:
        print("Voto obrigatório")
    else:
        print("Voto opcional")

eleicao()
