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

  it "is 'buzz' for 5" do
    expect(fizzbuzz(5)).to eq('buzz')
  end

  it "is 'fizz' for 6" do
    expect(fizzbuzz(6)).to eq('fizz')
  end
    
  it "is 'buzz' for 10" do
    expect(fizzbuzz(10)).to eq('buzz')
  end

  it "is 'fizzbuzz' for 15" do
    expect(fizzbuzz(15)).to eq('fizzbuzz')
  end

  it "is 'fizzbuzz' for 30" do
    expect(fizzbuzz(30)).to eq('fizzbuzz')
  end

  it "is 'fizzbuzz' for 45" do
    expect(fizzbuzz(45)).to eq('fizzbuzz')
  end


end

