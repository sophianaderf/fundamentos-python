def combustivel():
    distancia = float(input("Digite a distância percorrida em km: "))
    combustivel_carro = float(input("Digite a quantidade de combustível no tanque: "))
    combustivel_gasto = distancia / combustivel_carro
    return distancia, combustivel_carro, combustivel_gasto

distancia, combustivel_carro, combustivel_gasto = combustivel()
print(f"Distância percorrida em km: {distancia}")
print(f"Combustível no tanque: {combustivel_carro}")
print(f"Gasto em km: {combustivel_gasto}")