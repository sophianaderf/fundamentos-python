# Operador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input(f"Tem dinheiro para comprar? "))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"Vou comer um McDonald´s hoje? {autorizado}")

posso_comprar()