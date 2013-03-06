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
    else
        distancias.max
    end
end
