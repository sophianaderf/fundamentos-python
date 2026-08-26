def inverter_lista(lista):
    nova_lista = list(reversed(lista))
    return nova_lista
lista = ["Ana", "Bruno", "Carlos", "Laura"]
resultado = inverter_lista(lista)

print(f"Lista invertida: {resultado}")

inverter_lista(lista)