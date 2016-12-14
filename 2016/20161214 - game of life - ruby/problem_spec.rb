require_relative 'problem'

describe "problem" do
  it "sample" do
    bar = [[]]
    expect(problem(bar)).to eq([[]])
  end

  it "entra valor 1 apenas" do
    bar = [[1]]
    expect(problem(bar)).to eq([[0]])
  end


end
