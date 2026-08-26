def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)
    print(f"Ranking: {ranking}")

pontuacoes = [150, 320, 250, 480, 100, 390]

criar_ranking(pontuacoes)