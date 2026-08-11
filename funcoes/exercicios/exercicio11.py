def salario():
    valor_hora = float(input("Digite o valor do valor recebido por hora: "))
    quantidade_horas = float(input("Digite a quantidade de horas trabalhadas: "))
    salario = valor_hora * quantidade_horas
    return valor_hora, salario, quantidade_horas

valor_hora, valor_salario, quantidade_horas = salario()
print(f"Valor da hora: {valor_hora}")
print(f"Horas trabalhadas: {quantidade_horas}")
print(f"Salário do mês: {valor_salario}")