def avaliacao():
    nota = float(input("Digite sua nota: "))
    if nota >= 6:
        print(f"Nota: {nota}")
        print(f"Resultado final: Aprovado(a)")
    else:
        print(f"Nota: {nota}")
        print(f"Resultado final: Reprovado(a)")
    return nota
avaliacao()