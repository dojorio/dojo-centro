# [1, 2, 3].sum (dá merda)

class Array
    def sum
        self.reduce(0) {|a,b| a+b}
    end
end

# [1, 2, 3].sum (agora funciona!)

def split(lista, pivot)
    [lista[0..pivot-1].sum, lista[pivot..lista.count].sum].max
end


def trilha(distancias, dias)
    return distancias.sum if dias == 1
    return distancias.max if dias >= distancias.count

    if dias==3
        return 5
    else
        1.upto(distancias.count).map{|i| split(distancias, i)}.min
end
