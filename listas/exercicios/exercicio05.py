def remover_item(itens, posicao):
    removido = itens.pop(posicao)
    return removido


itens = ["Arroz", "Feijão", "Macarrão", "Leite"]

posicao = int(input("Digite a posição do item que deseja remover: "))

removido = remover_item(itens, posicao)

print(f"Item removido: {removido}")
print(f"Lista atualizada: {itens}")

removido = remover_item(itens, posicao)