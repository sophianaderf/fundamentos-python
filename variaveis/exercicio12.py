produto1 = 50
produto2 = 70
produto3 = 60
total = produto1 + produto2 + produto3
media = total / 3

print(f"O total da compra foi de R$ {total}")
print(f"Média de preço dos produtos: {media}")

if produto1 >= produto2 and produto1 >= produto3:
 print(f"Produto mais caro: {produto1}")
elif produto2 >= produto1 and produto2 >= produto3:
 print(f"Produto mais caro: {produto2}")
else:
 print(f"Produto mais caro: {produto3}")