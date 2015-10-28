require './fizzbuzz'

describe "FizzBuzz" do
  it "returns Fizz for 3" do
    expect(fizzbuzz(3)).to eq("Fizz")
  end

  it "returns 2 for 2" do
    expect(fizzbuzz(2)).to eq("2")
  end
end