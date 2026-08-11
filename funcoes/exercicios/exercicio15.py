def idade():
    idade_anos = int(input("Quantos anos você tem? "))
    idade_meses = idade_anos * 12
    idade_dias = idade_anos * 365
    return idade_anos, idade_meses, idade_dias

idade, idade_meses, idade_dias = idade()
print(f"Idade em anos: {idade}")
print(f"Idade em meses: {idade_meses}")
print(f"Idade em dias: {idade_dias}")
