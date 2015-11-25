require './folding'

describe "Folding" do
  it "is true for tape size 1 and in = out" do
    expect(fold_test([1],[1])).to eq(true)
  end

  it "is false for tapes size 1 and in != out" do
    expect(fold_test([1],[2])).to eq(false)
  end

  it "is false for tapes size 1 and in != out" do
    expect(fold_test([1],[3])).to eq(false)
  end

  it "is false for tapes size 1 and in != out" do
    expect(fold_test([1],[4])).to eq(false)
  end

  it "is false for tapes with in size 1 and out size 2" do
    expect(fold_test([1],[1,4])).to eq(false)
  end

  it "is true for tapes in[1,4] out[4,1]" do
    expect(fold_test([1,4],[4,1])).to eq(true)
  end

  it "is true for tapes in[1,4] out[4,1]" do
    expect(fold_test([1,4],[1,1])).to eq(false)
  end

end