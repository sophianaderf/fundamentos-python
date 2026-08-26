def remover_produto(produtos, produto):
    produtos.remove(produto)
    print(produtos)
produto = input("Digite o produto que deseja remover: ")
produtos = ["Arroz", "Feijão", "Macarrão", "Leite"]

remover_produto(produtos, produto)