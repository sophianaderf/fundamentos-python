def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    cliente = fila.pop(0)
    return cliente


fila = []

while True:
    cliente = input("Digite o nome do cliente ou 'n' para parar: ")

    if cliente == "n":
        break

    adicionar_cliente(fila, cliente)

print(f"Fila de atendimento: {fila}")

if len(fila) > 0:
    atendido = atender_cliente(fila)
    print(f"Cliente atendido: {atendido}")