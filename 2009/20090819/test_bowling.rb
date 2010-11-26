require 'rubygems'
require 'test/unit'
require 'bowling'

class BowlingTest < Test::Unit::TestCase
	def testJogoSemStrikeSemSpareRetornaPontuacaoTotal
		valoresDasJogadas = "523671"
		assert_equal(24, somatorioTotal(valoresDasJogadas))		
	end
	
	def testOutroJogoSemStrikeSemSpareRetornaPontuacaoTotal
		valoresDasJogadas = "523672"
		assert_equal(25, somatorioTotal(valoresDasJogadas))		
	end
	
	def testJogoSemStrikeComSpareRetornaPontuacaoTotal
		valoresDasJogadas = "5/3672"
		assert_equal(37, somatorioTotal(valoresDasJogadas))		
	end
	
	#def testCriaJogoApartirDeString
	#end
	
end