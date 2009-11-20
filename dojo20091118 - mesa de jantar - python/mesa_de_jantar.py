def avaliar_disposicao(entrada):
    a = []
    [a.extend(elemento) for elemento in entrada]
    participantes = set(a)
    
    mapa = dict()
    for paticipante in participantes:
        mapa[participante] = []
        for t in entrada:
            if participante in t:
                mapa[participante].extend(t)

        mapa[participante] = set(mapa[participante]).remove(participante)

     
    # lado_esquerdo = [item[0] for item in entrada]
    # lado_direito = [item[1] for item in entrada]
    
    # def nao_esta_no_lado_oposto(x):
        # return x not in lado_direito
    
    # return all( map( nao_esta_no_lado_oposto, lado_esquerdo) )
    
    # um amigo meu nao pode ser amigo de outro amigo meu