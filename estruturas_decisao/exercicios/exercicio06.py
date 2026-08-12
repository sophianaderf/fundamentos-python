def comparacao():
    numero_a = float(input("Digite o primeiro número (número A): "))
    numero_b = float(input("Digite o segundo número (número B): "))

    if numero_a > numero_b:
        print(f"{numero_a} (número A) é maior que {numero_b} (Número B. ")

    elif numero_a < numero_b:
        print(f"{numero_b} (número B) é maior que {numero_a} (número A). ")
    else:
        print(f"Os números são iguais.")
    return numero_a, numero_b
comparacao()