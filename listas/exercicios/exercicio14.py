def adicionar_produtos(compras, produtos):
    compras.extend(produtos)
    print(f"Lista de compras: {compras}")


def cancelar_compra(compras, produto):
    compras.remove(produto)
    print(f"Lista de compras atualizada: {compras}")


compras = ["Arroz", "Feijão", "Leite"]
produtos = ["Pão", "Café", "Açúcar"]

adicionar_produtos(compras, produtos)

produto = input("Digite o produto que deseja cancelar: ")

cancelar_compra(compras, produto)