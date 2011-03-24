class Jogada 
    def initialize(jogada, quem_ganha_de)
        @jogada = jogada
        @quem_ganha_de = quem_ganha_de
    end

    def empata_com?(jogada)
        @jogada == jogada.jogada
    end
    
    def ganha_de?(jogada)
        @quem_ganha_de[jogada] == @jogada
    end
end


class Jokenpo
    @@quem_ganha_de = { 
            "papel" => "tesoura",
            "tesoura" => "pedra",
            "pedra" => "papel"
    }

    def initialize(jogada1, jogada2)
        @jogada1 = Jogada.new(jogada1, @@quem_ganha_de)
        @jogada2 = Jogada.new(jogada2, @@quem_ganha_de)
    end

    def resultado
        if @jogada1.empata_com? @jogada2
            "empate"
        elsif @jogada1.ganha_de? @jogada2
            @jogada1.to_s
        else
            @jogada1.to_s
        end
    end
end


