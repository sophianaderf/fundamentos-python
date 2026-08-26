def adicionar_nota(notas, nota):
    notas.append(nota)
    print(f"Nota adicionada: {nota}")


def remover_nota(notas, nota):
    notas.remove(nota)
    print(f"Nota removida: {nota}")


def media_notas(notas):
    media = sum(notas) / len(notas)
    print(f"Média das notas: {media}")


notas = [7, 8, 9]

nova_nota = float(input("Digite uma nota para adicionar: "))
adicionar_nota(notas, nova_nota)

print(f"Notas atuais: {notas}")

nota_remover = float(input("Digite uma nota para remover: "))
remover_nota(notas, nota_remover)

print(f"Notas atuais: {notas}")

media_notas(notas)