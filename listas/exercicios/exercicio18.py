def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)
    return quantidade, soma, media, ordenadas

temperaturas = [25, 30, 22, 28, 24, 31]

quantidade, soma, media, ordenadas = analisar_temperaturas(temperaturas)

print(f"Quantidade de temperaturas: {quantidade}")
print(f"Soma das temperaturas: {soma}")
print(f"Média das temperaturas: {media}")
print(f"Temperaturas ordenadas: {ordenadas}")

analisar_temperaturas(temperaturas)