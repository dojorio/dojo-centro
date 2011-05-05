def placar(jogo):
    bonus = 0
    
    for i in range(0, 10):
        rodada = jogo[i]
        is_spare = (sum(rodada) == 10)
        if is_spare:
            proxima_rodada = jogo[i+1]
            bonus += proxima_rodada[0]

    return sum(sum(jogo[0:10], ())) + bonus