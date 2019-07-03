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

  it "with 4" do
    expect(fizzbuzz(4)).to eq(4)
  end

  it "with 5" do
    expect(fizzbuzz(5)).to eq("buzz")
  end

  it "with 6" do
    expect(fizzbuzz(6)).to eq("fizz")
  end
  it "with 7" do
    expect(fizzbuzz(7)).to eq(7)
  end
   it "with 10" do
    expect(fizzbuzz(10)).to eq('buzz')
  end
end
