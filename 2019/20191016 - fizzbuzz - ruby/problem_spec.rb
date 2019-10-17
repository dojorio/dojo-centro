require_relative 'problem'

describe "FizzBuzz" do
  it "retorna 1 quando passa 1" do
    expect(fizzbuzz(1)).to eq(1)
  end
  it "retorna 2 quando passa 2" do
  	expect(fizzbuzz(2)).to eq(2)
  end
  it "retorna fizz quando passa 3" do
  	expect(fizzbuzz(3)).to eq('fizz')
  end
  it "retorna 4 quando passa 4" do
  	expect(fizzbuzz(4)).to eq(4)
  end
  it "retorna buzz quando passa 5" do
  	expect(fizzbuzz(5)).to eq('buzz')
  end
  it "retorna fizz quando passa 6" do
  	expect(fizzbuzz(6)).to eq('fizz')
  end
  it "retorna 7 quando passa 7" do
  	expect(fizzbuzz(7)).to eq(7)
  end
  it "retorna 8 quando passa 8" do
  	expect(fizzbuzz(8)).to eq(8)
  end
  it "retorna fizz quando passa 9" do
  	expect(fizzbuzz(9)).to eq("fizz")
  end
end
