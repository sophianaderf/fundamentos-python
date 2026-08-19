def somar_numeros():
    numero = int(input("Digite um número inteiro para calcular a soma dos números até ele: "))
    total = 0
    for valor in range(1, numero):
        total += valor
    print(total)
    
somar_numeros()