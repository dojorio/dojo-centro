require_relative 'problem'

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1110

describe "problem" do
  it "tres cartas" do
    expect(cartasfora(3)).to eq([[1, 3], 2])
  end

  it "quatro cartas" do
    expect(cartasfora(4)).to eq([[1, 3, 2], 4])
  end

  it "cinco cartas" do
    expect(cartasfora(5)).to eq([[1, 3, 5, 4], 2])
  end  

  it "seis cartas" do
    expect(cartasfora(6)).to eq([[1, 3, 5, 2, 6], 4])
  end

   it "sete cartas" do
    expect(cartasfora(7)).to eq([[1, 3, 5, 7, 4, 2], 6])
  end

  it "dezenove cartas" do
  	expect(cartasfora(19)).to eq([[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14], 6])
  end		
end
