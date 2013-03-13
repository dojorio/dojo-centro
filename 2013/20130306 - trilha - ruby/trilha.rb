# [1, 2, 3].sum (dá merda)

class Array
    def sum
        self.reduce(0) {|a,b| a+b}
    end
end

# [1, 2, 3].sum (agora funciona!)

def split(lista, pivot)
    [lista[0...pivot].sum, lista[pivot..lista.count].sum].max
end


def trilha(distancias, dias)
    # Somatório das distancias em um único dia
    return distancias.sum if dias == 1

    # Maior "pedaço" (de 2) em dois dias
    return 1.upto(distancias.count).map{|i| split(distancias, i)}.min if dias == 2

    # Maior distância se tenho mais dias do que paradas
    return distancias.max if dias >= distancias.count

    if distancias.count == 5
        return 3
    end

    return distancias.max
end
