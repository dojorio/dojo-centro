class Array
    def sum
        self.reduce(0) {|a,b| a+b}
    end
end

def trilha(distancias, dias)
    if dias == 1
        distancias.sum
    else
        distancias.max
    end

end
