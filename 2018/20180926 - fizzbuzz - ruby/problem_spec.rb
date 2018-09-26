require_relative 'problem'

#http://www.dojopuzzles.com/problemas/exibe/fizzbuzz/

describe "fizzbuzz" do
  it "1 is 1" do
    expect(fizzbuzz(1)).to eq(1)
  end

  it "2 is 2" do
    expect(fizzbuzz(2)).to eq(2)
  end

  it "3 is 'fizz'" do
    expect(fizzbuzz(3)).to eq('fizz')
  end
end
