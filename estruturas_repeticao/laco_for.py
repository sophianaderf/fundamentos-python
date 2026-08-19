# Laço for simples
import time

def mostrar_numero():
    for i in range(1, 6):
        print(f"O número atual é {i}")
        time.sleep(5)



#mostrar_numero()

def mostrar_numero_alternado():
    for num in range (0, 20, 2):
        print(f"O número é {num}")

#mostrar_numero_alternado()

def somar_numeros():
    total = 0
    for valor in range(1, 20):
        total += valor
    print(total)

#somar_numeros()

def mostrar_numeros_pares():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f"numeros pares {numero}")

#mostrar_numeros_pares()

def mostrar_item_da_lista():
    sacola_de_frutas = ["Maçã", "Uva", "Melancia", "Banana"]
    for frutas in sacola_de_frutas:
        print(f"Na minha sacola contém {frutas}")

#mostrar_item_da_lista()


def laco_aninhado():
    nomes = ["Sophia", "Sara", "Laura"]
    notas = [9, 10, 10]
    for nome in nomes:
        print(f"Nome do aluno: {nome}")
        for nota in notas:
            print(f"Nota do aluno: {nota}")

laco_aninhado()