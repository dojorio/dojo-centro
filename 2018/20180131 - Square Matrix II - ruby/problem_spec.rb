require_relative 'problem'

describe "problem" do
  it "matriz 1" do
    order = 1
    expec = [[1]]
    expect(problem(order)).to eq(expec)
  end

  it "matriz 2" do
    order = 2
    expec = [[1, 2], 
    		 [2, 1]]
    expect(problem(order)).to eq(expec)
  end

  it "matriz 3" do
    order = 3
    expec = [[1, 2, 3], 
    		 [2, 1, 2],
    		 [3, 2, 1]]
    expect(problem(order)).to eq(expec)
  end
end
