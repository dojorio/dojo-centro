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

  it "is Fizz with 6" do
    expect(fizzbuzz(6)).to eq("Fizz")
  end

  it "is Fizz with 9" do
    expect(fizzbuzz(9)).to eq("Fizz")
  end

  it "is Fizz with 10" do
    expect(fizzbuzz(10)).to eq("Buzz")
  end

  it "is FizzBuzz with 15" do
    expect(fizzbuzz(15)).to eq("FizzBuzz")
  end

  it "is FizzBuzz with 60" do
    expect(fizzbuzz(60)).to eq("FizzBuzz")
  end
end