require_relative 'problem'

describe "FizzBuzz" do
  it "retorna 1 quando passa 1" do
    expect(fizzbuzz(1)).to eq(1)
  end
  it "retorna 2 quando passas 2" do
  	expect(fizzbuzz(2)).to eq(2)
  end
end
