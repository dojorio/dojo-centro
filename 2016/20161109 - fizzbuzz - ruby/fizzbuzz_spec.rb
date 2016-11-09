require_relative 'fizzbuzz'

describe "fizzbuzz" do
  it "is 1 for 1" do
    expect(fizzbuzz(1)).to eq(1)
  end

  it "is fizz for 3" do
    expect(fizzbuzz(3)).to eq("fizz")
  end
end
