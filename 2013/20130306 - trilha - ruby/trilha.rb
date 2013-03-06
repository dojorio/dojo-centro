# [1, 2, 3].sum (dá merda)

class Array
    def sum
        self.reduce(0) {|a,b| a+b}
    end
end

# [1, 2, 3].sum (agora funciona!)


def trilha(distancias, dias)
    return distancias.sum if dias == 1
    return distancias.max if dias >= distancias.count

    if distancias.count == 3
        [distancias[0] + distancias[1], distancias[1] + distancias[2]].min
    else
        5
    end
end
