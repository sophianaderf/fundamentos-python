def mostrar_primos():
    inicio = int(input("Digite o primeiro número: "))
    fim = int(input("Digite o segundo número: "))

    for numero in range(inicio, fim + 1):
        if numero < 2:
            continue

        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

        if primo:
            print(numero)


mostrar_primos()