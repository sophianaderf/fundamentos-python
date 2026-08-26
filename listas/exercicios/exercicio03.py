def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(convidados)

convidados = ["Ana", "Carlos", "Mariana"]
novos_convidados = ["João", "Sophia", "Laura"]

adicionar_convidados(convidados, novos_convidados)