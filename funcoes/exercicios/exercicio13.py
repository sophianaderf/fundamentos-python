def pagamento():
    salario_fixo = float(input("Digite o salário fixo: "))
    vendas = float(input("Digite o valor das vendas do mês: "))
    comissao = float(input("Digite o valor do comissão por venda: "))
    pagamento_final = salario_fixo + (vendas * comissao)
    return salario_fixo, vendas, comissao, pagamento

salario_fixo, vendas, comissao, pagamento_final = pagamento()
print(f"Salário fixo: {salario_fixo}")
print(f"Valor total das vendas: {vendas}")
print(f"Valor total das comissões: {comissao}")
print(f"Valor total do pagamento do mês: {pagamento}")