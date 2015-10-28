require './fizzbuzz'

describe "FizzBuzz" do
  it "returns Fizz for 3" do
    expect(fizzbuzz(3)).to eq("Fizz")
  end

  it "returns 2 for 2" do
    expect(fizzbuzz(2)).to eq("2")
  end

  it "returns 1 for 1" do
    expect(fizzbuzz(1)).to eq("1")
  end

  it "returns 4 for 4" do
    expect(fizzbuzz(4)).to eq("4")
  end

  it "returns Buzz for 5" do
    expect(fizzbuzz(5)).to eq("Buzz")
  end

  it "returns Fizz for 6" do
    expect(fizzbuzz(6)).to eq("Fizz")
  end

  it "returns Fizz for 9" do
    expect(fizzbuzz(9)).to eq("Fizz")
  end

  it "returns Buzz for 10" do
    expect(fizzbuzz(10)).to eq("Buzz")
  end

  it "returns Fizz for 12" do
    expect(fizzbuzz(12)).to eq("Fizz")
  end
end