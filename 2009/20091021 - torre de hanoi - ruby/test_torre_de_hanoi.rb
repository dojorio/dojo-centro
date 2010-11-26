require 'rubygems'
require 'test/unit'
require 'torre_de_hanoi'

class TorreDeHanoiTest < Test::Unit::TestCase
	
	def	test_1_disco_de_1_na_posicao_A
		entradas = [1, 0, 0]
        saidas = ["1 to c"]
		assert_equal(saidas, resolver(entradas))
	end

	# def	test_1_disco_de_1_na_posicao_B
		# entradas =  [[0, 1, 0],[21, 0, 0]]
        # saidas = [["1 to c"], ["1 to b","2 to c","1 to c"]]
        
        # [entradas, saidas].each do |entrada,saida|
            # assert_equal(resolver(entrada), saida)
        # end
            
	# end
    
	def	test_disco_de_1_na_posicao_A_e_disco_de_2_na_posicao_B
		entradas = [1, 2, 0]
        saidas = []
        saidas << "2 to c"
        saidas << "1 to c"
		assert_equal(saidas, resolver(entradas))
	end
    
    def test_disco_de_2_e_disco_de_1_na_posicao_A
        entradas = [21, 0, 0]
        saidas = []
        saidas << "1 to b"
        saidas << "2 to c"
        saidas << "1 to c"
		assert_equal(saidas, resolver(entradas))
    end

    def test_disco_de_3_de_2_e_disco_de_1_na_posicao_A
        entradas = [321, 0, 0]
        saidas = []
        saidas << "1 to c"
        # saidas << "2 to b"
        # saidas << "1 to b"
        # saidas << "3 to c"
        # saidas << "1 to a"
        # saidas << "2 to c"
        # saidas << "1 to c"
		assert_equal(saidas, resolver(entradas))
    end

end