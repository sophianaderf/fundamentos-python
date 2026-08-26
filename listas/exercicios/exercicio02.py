def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print(alunos)
nome = input("Digite o nome do aluno: ")
posicao = int(input("Digite a posição: "))
alunos = ["Sophia", "Mayara", "Laura"]

inserir_aluno(alunos, nome, posicao)