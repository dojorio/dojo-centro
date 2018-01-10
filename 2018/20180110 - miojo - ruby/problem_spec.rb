require_relative 'problem'

describe "problem" do
  it "duas de 3" do
    expect(problem(3,3)).to eq(3)
  end

  it "2 e 5" do
    expect(problem(2,5)).to eq(5)
  end
# 
end
