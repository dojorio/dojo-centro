# [1, 2, 3].sum (dá merda)

class Array
    def sum
        self.reduce(0) {|a,b| a+b}
    end
end

# [1, 2, 3].sum (agora funciona!)

def split(distancias, i)
    [distancias[0..i-1].sum, distancias[i..distancias.count].sum].max
end


def trilha(distancias, dias)
    return distancias.sum if dias == 1
    return distancias.max if dias >= distancias.count

    1.upto(distancias.count).map{|i| split(distancias, i)}.min
end
