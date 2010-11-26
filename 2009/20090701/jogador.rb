class JogadorExpulsoException < StandardError
    
end

class Jogador
    attr_accessor :cartoes
    
    def initialize
        @cartoes = []        
    end

    def cometer_falta (jogador, options = {})
        raise JogadorExpulsoException if expulso?
        cartao = cartao_cor (options[:tipo])
        @cartoes << cartao unless cartao.nil?
    end
    
    def cartao_cor (tipo)
        if (tipo == :grave)
            if @cartoes == ['amarelo']
                return ['amarelo', 'vermelho']
            end
            return 'amarelo'
            
        elsif (tipo == :gravissima)
            return 'vermelho'            
        end
    end
    
    def expulso?
         @cartoes.include?('vermelho')
    end
end
