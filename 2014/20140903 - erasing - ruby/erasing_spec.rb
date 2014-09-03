require './erasing'

describe "Erasing" do
  it "10 1" do
    expect(erasing(10, 1)).to eq(1)
  end

  it "20 1" do
    expect(erasing(20, 1)).to eq(2)
  end

  it "30 1" do
    expect(erasing(30, 1)).to eq(3)
  end

  it "40 1" do
    expect(erasing(40, 1)).to eq(4)
  end

  it "12 1" do
    expect(erasing(12, 1)).to eq(2)
  end

  it "13 1" do
    expect(erasing(13, 1)).to eq(3)
  end
end