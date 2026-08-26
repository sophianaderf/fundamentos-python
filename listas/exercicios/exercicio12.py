def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    return media
notas = [8, 7, 9, 10]
resultado = calcular_media(notas)

print(f"Média das notas: {resultado}")

calcular_media(notas)