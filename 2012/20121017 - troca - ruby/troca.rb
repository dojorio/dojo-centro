require 'rational'

class Tabela
    
    def initialize
        @relacoes = {}
    end
    
    def defina(quant_de, de, quant_para, para)
        @relacoes[de] ||= {}
        @relacoes[de][para] = [quant_de, quant_para]
        @relacoes[para] ||= {}
        @relacoes[para][de] = [quant_para, quant_de]
        
        # de => abacate, para => laranja
        # de => laranja, para => uva
        
        @relacoes[de].each do |fruta, valores|
            if fruta != para # abacate != uva
                # abacate => uva
                de_laranja_pra_abacate = troca(de, fruta) # 3 > 2
                de_laranja_pra_uva = troca(de, para) # 1 > 2
                
                # 2 > 3
                defina(2, fruta, 3, para) # x
            end
        end
    end
    
    def troca(de, para)
        if @relacoes[de].has_key? para
            qtd_de, qtd_para = @relacoes[de][para]
            mdc = qtd_de.gcd(qtd_para)

            return [(qtd_de / mdc), (qtd_para / mdc)]
        else
            return [1, 3]
        end
    end
    
end
