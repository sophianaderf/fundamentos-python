def numeros():
    a_antes = int(input("Digite um número inteiro: "))
    b_antes = int(input("Digite outro númro inteiro: "))

    a_depois = b_antes
    b_depois = a_antes
    return a_antes, b_antes, a_depois, b_depois

a_antes, b_antes, a_depois, b_depois = numeros()
print(f"Antes: ")
print(f"A = {a_antes}")
print(f"B = {b_antes} ")
print(f"Depois: ")
print(f"A = {a_depois}")
print(f"B = {b_depois}")