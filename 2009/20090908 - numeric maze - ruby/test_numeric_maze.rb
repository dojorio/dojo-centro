require 'rubygems'
require 'test/unit'
require 'numeric_maze'

class NumericMazeTest < Test::Unit::TestCase
	
	def	test_2_4
		path = solve(2, 4)
		assert_equal(path, [2, 4])
	end

	def	test_2_8_returns_2_4_8
		path = solve(2, 8)
		assert_equal(path, [2, 4, 8])
	end
	def	test_1_8_returns_1_2_4_8
		path = solve(1, 8)
		assert_equal(path, [1, 2, 4, 8])
	end
	
	def	test_potenciaDe2_potenciaDe2_returns_caminho_curto
		path = solve(1, 16)
		assert_equal(path, [1, 2, 4, 8,16])
	end
	
	def	test_1_3_returns_1_3
		path = solve(1, 3)
		assert_equal(path, [1,3])
	end
	
	def	test_1_6_returns_1_3_6
		path = solve(1, 6)
		assert_equal(path, [1, 3, 6])
	end
	
	def test_2_6_returns_2_4_6
		path = solve(2, 6)
		assert_equal(path, [2, 4, 6])
	end
	
end