def situacao():
    nota = float(input("Qual a nota do aluno? "))
    if nota >= 0 and nota <= 4:
        print(f"Nota do aluno: {nota}")
        print("FInsuficiente")
    elif nota >= 5 and nota <= 6:
        print(f"Nota do aluno: {nota}")
        print("Regular")
    elif nota >= 7 and nota <= 8:
        print(f"Nota do aluno: {nota}")
        print("Bom")
    else:
        print(f"Nota do aluno: {nota}")
        print("Excelente!")
    return nota

situacao()