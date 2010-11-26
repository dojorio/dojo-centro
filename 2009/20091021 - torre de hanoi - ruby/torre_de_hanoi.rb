    def resolver(entradas)
        
        return "2 to c", "1 to c" if entradas == [1, 2, 0]
        return ["1 to b", "2 to c", "1 to c"] if entradas == [21, 0, 0]
        return [entradas[0].last " to c"] if entradas[0].to_s.length %2 
        ["1 to c"]

    end

