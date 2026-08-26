def adicionar_nome(nomes):
    while True:
        nome = input("Digite um nome para adicionar (ou 'n' para parar): ")

        if nome == "n":
            break
        nomes.append(nome)
    print(f"Nomes: {nomes}")


nomes = []
adicionar_nome(nomes)