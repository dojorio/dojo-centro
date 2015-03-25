require './fizzbuzz'

describe "fizzbuzz" do
  it "is 1 with 1" do
    expect(fizzbuzz(1)).to eq(1)
  end

  it "is 2 with 2" do
    expect(fizzbuzz(2)).to eq(2)
  end

  it "is Fizz with 3" do
    expect(fizzbuzz(3)).to eq("Fizz")
  end

  it "is Buzz with 5" do
    expect(fizzbuzz(5)).to eq("Buzz")
  end
end