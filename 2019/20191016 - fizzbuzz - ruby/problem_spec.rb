require_relative 'problem'

describe "FizzBuzz" do
  it "retorna 1 quando passa 1" do
    expect(fizzbuzz(1)).to eq(1)
  end
end
