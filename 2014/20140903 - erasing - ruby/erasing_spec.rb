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

  it "14 1" do
    expect(erasing(14, 1)).to eq(4)
  end

  it "18 1" do
    expect(erasing(18, 1)).to eq(8)
  end

  it "666 1" do
    expect(erasing(666, 1)).to eq(66)
  end

  it "123 1" do
    expect(erasing(123, 1)).to eq(23)
  end

  it "321 1" do
    expect(erasing(321, 1)).to eq(32)
  end

  it "331 1" do
    expect(erasing(331, 1)).to eq(33)
  end

  it "313 1" do
    expect(erasing(313, 1)).to eq(33)
  end

  it "1000 1" do
    expect(erasing(1000, 1)).to eq(100)
  end

  it "9696 1" do
    expect(erasing(9696, 1)).to eq(996)
  end
end