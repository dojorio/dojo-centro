require_relative 'problem'

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1110

describe "problem" do
  it "tres cartas" do
  	# 1 2 3
  	# 1, 3
  	# 2
    expect(cartasfora(3)).to eq([[1, 3], 2])
  end

  it "quatro cartas" do
  	# 1 2 3 4
  	# 1, 3, 2
  	# 4
    expect(cartasfora(4)).to eq([[1, 3, 2], 4])
  end  
end
