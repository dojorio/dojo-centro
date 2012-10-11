def tempo_minimo_de_preparo(miojo, ampulhetas)    
    max = [ampulhetas.min, ampulhetas.max / ampulhetas.min].max
    
    # O(caralho!)
    # regra geral: quando |Ax - ay| == miojo
    # retorna max(Ax,ay)
    
    1.upto(max) do |x|
        1.upto(max) do |y|
            azaox = ampulhetas.min * x
            azinhoy = ampulhetas.max * y
            tempo = ( azaox - azinhoy ).abs
            return [azaox, azinhoy].max if tempo == miojo
        end
    end
    
    false
end
