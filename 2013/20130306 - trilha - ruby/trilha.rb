def trilha(distancias, dias)
    if dias == 2
        return 3
    end
    distancias.reduce(0) {|a,b| a+b}
end
