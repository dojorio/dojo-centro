require './fizzbuzz'

describe "fizzbuzz" do
  it "is 1 with 1" do
    expect(fizzbuzz(1)).to eq(1)
  end

  it "is 2 with 2" do
    expect(fizzbuzz(2)).to eq(2)
  end
end