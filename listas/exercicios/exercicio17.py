def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print(f"Produto vendido: {produto}")
    else:
        print(f"O produto {produto} não está disponível.")
    return estoque

estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]
produto = input("Digite o produto que deseja comprar: ")
resultado = vender_produto(estoque, produto)

print(f"Estoque atualizado: {resultado}")