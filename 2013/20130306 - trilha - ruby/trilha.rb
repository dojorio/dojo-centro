# [1, 2, 3].sum (dá merda)

class Array
    def sum
        self.reduce(0) {|a,b| a+b}
    end
end

# [1, 2, 3].sum (agora funfa!)


def trilha(distancias, dias)
    if dias == 1
        distancias.sum
    elsif distancias.count == 3
        [distancias[0] + distancias[1], distancias[1] + distancias[2]].min
    else
        distancias.max
    end
end
