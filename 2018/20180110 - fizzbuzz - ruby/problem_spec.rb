require_relative 'problem'

describe "Fizzbuzz" do
  it "is 1 for 1" do
    expect(fizzbuzz(1)).to eq(1)
  end

  it "is 2 for 2" do
    expect(fizzbuzz(2)).to eq(2)
  end

  it "is 7 for 7" do
    expect(fizzbuzz(7)).to eq(7)
  end

  it "is 'fizz' for 3" do
    expect(fizzbuzz(3)).to eq('fizz')
  end
end
