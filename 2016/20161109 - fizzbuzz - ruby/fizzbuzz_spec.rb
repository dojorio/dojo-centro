require_relative 'fizzbuzz'

describe "fizzbuzz" do
  it "is 1 for 1" do
    expect(fizzbuzz(1)).to eq(1)
  end

  it "is 2 for 2" do
    expect(fizzbuzz(2)).to eq(2)
  end
  
  it "is fizz for 3" do
    expect(fizzbuzz(3)).to eq("fizz")
  end

  it "is 4 for 4" do
    expect(fizzbuzz(4)).to eq(4)
  end

end
