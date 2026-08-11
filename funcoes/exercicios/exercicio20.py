def dados():
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual a sua idade? "))
    profissao = input("Qual a sua profissão? ")
    cidade = input("Qual a sua cidade? ")

    return nome, idade, profissao, cidade

nome, idade, profissao, cidade = dados()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Profissao: {profissao}")
print(f"Cidade: {cidade}")