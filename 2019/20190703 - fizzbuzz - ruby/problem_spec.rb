require_relative 'problem'

describe "fizzbuzz" do
  it "with 1" do
    expect(fizzbuzz(1)).to eq(1)
  end

  it "with 2" do
    expect(fizzbuzz(2)).to eq(2)
  end

  it "with 3" do
    expect(fizzbuzz(3)).to eq("fizz")
  end
end
