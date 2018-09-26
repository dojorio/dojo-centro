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

   it "4 is 4 " do
    expect(fizzbuzz(4)).to eq(4)
  end

  it "5 is 5 " do
    expect(fizzbuzz(5)).to eq('buzz')
  end

  it "6 is 6 " do
    expect(fizzbuzz(6)).to eq('fizz')
  end

  it "7 is 7 " do
    expect(fizzbuzz(7)).to eq(7)
  end

  it "8 is 8 " do
    expect(fizzbuzz(8)).to eq(8)
  end

  it "9 is 'fizz'" do
    expect(fizzbuzz(9)).to eq('fizz')
  end

    it "10 is 'buzz'" do
    expect(fizzbuzz(10)).to eq('buzz')
  end
end
