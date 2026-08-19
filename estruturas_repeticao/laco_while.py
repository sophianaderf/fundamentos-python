def mostrar_numero_while():
    contador = 0
    while contador <= 10:
        contador += 1
        print(f"Contagem atual: {contador}")

#mostrar_numero_while()

def contagem_regressiva():
    valor_contagem = int(input("Digite um número maior que 10: "))
    if valor_contagem < 10:
        print("Valor inválido")
    else:
        while valor_contagem >= 1:
            print(f"Contagem regressiva: {valor_contagem}")
            valor_contagem -= 1
        print("Contagem finalizada.")

#contagem_regressiva()

def soma_finita():
    while True:
        num_1 = int(input("Digite o primeiro valor: "))
        num_2 = int(input("Digite o segundo valor: "))

        if num_1 == 0:
            print("Função de soma encerrada")

            break
        else:
            soma = num_1 + num_2
            print(f"O Resultado da soma é {soma}")

soma_finita()
