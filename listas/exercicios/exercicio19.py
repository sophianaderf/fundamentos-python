def sistema_notas(notas):
    notas.append(8.0)
    notas.insert(2, 10.0)
    notas.extend([6.5, 7.0])
    notas.remove(5.5)

    ultima = notas.pop()
    posicao = notas.index(8.5)
    quantidade = len(notas)
    ordenadas = sorted(notas)
    inversas = list(reversed(notas))
    soma = sum(notas)
    media = sum(notas) / len(notas)

    print(notas)
    print(ultima)
    print(posicao)
    print(quantidade)
    print(ordenadas)
    print(inversas)
    print(soma)
    print(media)


notas = [7.5, 6.0, 8.5, 9.0, 5.5]

sistema_notas(notas)