require './folding'

describe "Folding" do
  it "is true for tape size 1 and in = out" do
    expect(fold_test([1],[1])).to eq(true)
  end

  it "is false for tapes size 1 and in != out" do
    expect(fold_test([1],[2])).to eq(false)
  end

  it "is false for tapes in[1] out[3]" do
    expect(fold_test([1],[3])).to eq(false)
  end

  it "is false for tapes in[1] out[4]" do
    expect(fold_test([1],[4])).to eq(false)
  end

  it "is false for tapes in[1] out[1,4]" do
    expect(fold_test([1],[1,4])).to eq(false)
  end

  it "is true for tapes in[1,4] out[4,1]" do
    expect(fold_test([1,4],[4,1])).to eq(true)
  end

  it "is true for tapes in[1,4] out[4,1]" do
    expect(fold_test([1,4],[1,1])).to eq(false)
  end

  it "is true for tapes in[1,2] out[3]" do
    expect(fold_test([1,2],[3])).to eq(true)
  end

  it "is false for tapes in[1,2] out[4]" do
    expect(fold_test([1,2],[4])).to eq(false)
  end

  it "is false for tapes in[1,2] out[3,0]" do
    expect(fold_test([1,2],[3,0])).to eq(false)
  end

  it "is false for tapes in[1,1,1] out[3,1]" do
    expect(fold_test([1,1,1],[3,1])).to eq(false)
  end

  it "is true for tapes in[1,1,1,0] out[3,0]" do
    expect(fold_test([1,1,1,0],[3,0])).to eq(true)
  end
end