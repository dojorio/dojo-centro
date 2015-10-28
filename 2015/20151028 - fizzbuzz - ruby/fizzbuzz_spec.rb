require './fizzbuzz'

describe "FizzBuzz" do
  it "returns Fizz for 3" do
    expect(fizzbuzz(3)).to eq("Fizz")
  end
end