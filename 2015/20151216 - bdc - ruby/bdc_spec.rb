require_relative 'bdc'

describe "BDC" do
  it "1x1 and size 1 grid 0" do
    expect(bdc(1, [[0]])).to eq(0)
  end

  it "1x1 and size 1 grid 1" do
    expect(bdc(1, [[1]])).to eq(1)
  end

  it "1x1 and size >1 grid 1" do
    expect(bdc(2, [[1]])).to eq(0)
  end
end
