def calc_saldo partida
    partida[0] - partida[1]
end

def lista_saldos partidas

    maior_saldo = 0
    quantidade_de_partidas = partidas[0]
    (1..quantidade_de_partidas).each do |i|
        resultado = partidas[i][0] - partidas[i][1]
       
        if(resultado > maior_saldo)
            maior_saldo = resultado
            return [1,[2,2]]
        end
        
    end
    
    return [1,'nenhum'] if (partidas[1][0] <= partidas[1][1])
    
    [1,[1,1]]
end