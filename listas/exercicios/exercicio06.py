def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    return posicao
produto = input("Digite o produto que deseja encontrar: ")
produtos = ["Arroz", "Feijão", "Macarrão", "Leite"]
posicao = encontrar_produto(produtos, produto)

print(f"O produto está na posição: {posicao}")

encontrar_produto(produtos, produto)