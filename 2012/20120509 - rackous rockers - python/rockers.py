def rock(cds, size, songs):
    vetor = [0] * (sum(songs)+1)
    for song in songs:
        for i in range(len(vetor)-1,-1,-1):
            v = vetor[i]
            if v > 0:
                vetor[song + i] = max(vetor[song + i], v+1)        
        vetor[song] = max(vetor[song],1)
        
    print vetor
    return max(vetor[0:cds*size+1])
