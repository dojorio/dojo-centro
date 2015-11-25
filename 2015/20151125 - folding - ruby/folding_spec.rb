require './folding'

describe "Folding" do
  it "is true for tape size 1 and in = out" do
    expect(fold_test([1],[1])).to eq(true)
  end

  it "is false for tapes size 1 and in != out" do
    expect(fold_test([1],[2])).to eq(false)
  end
end