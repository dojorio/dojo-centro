require 'rubygems'
require 'test/unit'
require 'jogador'

class JogadorTest < Test::Unit::TestCase

    def setup
        @edmundo = Jogador.new
        @richarlysson = Jogador.new
    end

    def test_falta_grave_recebe_amarelo
        @edmundo.cometer_falta(@richarlysson, :tipo => :grave)
        assert @edmundo.cartoes.include?("amarelo")
    end
    
    def test_duas_faltas_graves_recebe_vermelho
        @edmundo.cometer_falta(@richarlysson,:tipo => :grave)
        @edmundo.cometer_falta(@richarlysson,:tipo => :grave)
        assert_equal ["amarelo", "amarelo", "vermelho"], @edmundo.cartoes,
        "Jogador possui cartoes #{@edmundo.cartoes.to_s}"
    end
    
    def test_falta_gravissima_recebe_vermelho
        @edmundo.cometer_falta(@richarlysson, :tipo => :gravissima)
        assert @edmundo.cartoes.include?("vermelho")
    end
    
    def test_falta_leve_nao_recebe_cartao
        cartoes = @edmundo.cartoes
        @edmundo.cometer_falta(@richarlysson)
        assert_equal cartoes, @edmundo.cartoes
    end
    
    def test_falta_leve_com_cartao
        @edmundo.cometer_falta(@richarlysson, :tipo => :grave)
        cartoes = @edmundo.cartoes        
        @edmundo.cometer_falta(@richarlysson)
        assert_equal cartoes, @edmundo.cartoes
    end
        
    def test_cartao_vermelho_eh_expulso
        @edmundo.cometer_falta(@richarlysson, :tipo => :gravissima)
        assert @edmundo.expulso?
    end
    
    def test_raises_jogador_recebeu_3_cartoes
        @edmundo.cometer_falta(@richarlysson, :tipo => :grave)
        @edmundo.cometer_falta(@richarlysson, :tipo => :grave)
        assert_raises JogadorExpulsoException do
            @edmundo.cometer_falta(@richarlysson, :tipo => :grave)       
        end
    end   
end

