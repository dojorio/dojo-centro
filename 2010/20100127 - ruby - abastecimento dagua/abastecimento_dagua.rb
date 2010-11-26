class Bomba
    attr_accessor :quebrada
    
    # def quebrada=(quebrada)
        # @quebrada = quebrada
    # end
  
end

class SistemaAbastecimento
  
    attr_accessor :faltou_agua_da_rua
  
    def executa(agua_da_rua, bomba_do_poco, cisterna)
      true
    end

    def bomba_do_poco_ligada?
      false
    end

end

class Caixa
    attr_accessor :limite_minimo
end