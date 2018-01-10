require_relative 'problem'

describe "problem" do

  it "duas de 3" do
    expect(problem(3,3)).to eq(3)
  end

  it "2 e 5" do
    expect(problem(2,5)).to eq(5)
  end

  it "5 e 2" do
    expect(problem(5,2)).to eq(5)
  end

  it "7 e 4" do
    expect(problem(7,4)).to eq(7)
  end

  it "4 e 7" do
    expect(problem(4,7)).to eq(7)
  end
  
  it "5 e 8" do
    expect(problem(5,8)).to eq(8)
  end

  it "4 e 5" do
    expect(problem(4,5)).to eq(8)
  end

  it "2 e 9" do
    expect(problem(2,9)).to eq(9)
  end

  it "3 e 9" do
    expect(problem(3,9)).to eq(3)
  end

  it "7 e 5" do
    expect(problem(7,5)).to eq(10)
  end

end
