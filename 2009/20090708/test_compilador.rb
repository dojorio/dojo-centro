require 'rubygems'
require 'test/unit'
require 'compilador'

class AssertionsTest < Test::Unit::TestCase

    def test_mostra_cadeia_de_caracteres
        @comando = "mostra('Dojo Rio')"
        assert_equal "print 'Dojo Rio'", traduz(@comando)
    end
    
    def test_mostra_inteiro
        @comando = "mostra(0)"
        assert_equal "print 0", traduz(@comando)
    end
    
    def test_atribuicao_inteiro
        @comando = "a = 1"
        assert_equal "a = 1", traduz(@comando)
    end
    
    def test_mostra_variavel
        @comando = "mostra(variavel)"
        assert_equal "print variavel", traduz(@comando)
    end
    
    def test_mostra_numero_de_ponto_flutuante
        @comando = "mostra(3.3)"
        assert_equal "print 3.3", traduz(@comando)
    end
    
    def test_condicional
        @comando = "se Verdadeiro:"
        assert_equal "if True:", traduz(@comando)
    end
end
