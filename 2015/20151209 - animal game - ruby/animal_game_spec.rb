require_relative 'animal_game'

describe "Animal game" do
  it "gives zero if no combination is found" do
    expect(prize(1, 1234, 0)).to eq(0)
  end

  it "gives 16x value if is from same group 1" do
    expect(prize(1, 1299, 0)).to eq(16)
  end

  it "gives 16x value if is from same group 2" do
    expect(prize(2, 1299, 0)).to eq(32)
  end

  it "gives 16x value if is from same group 3" do
    expect(prize(2, 1297, 0)).to eq(32)
  end

  it "gives 16x value if is from same group 4" do
    expect(prize(2, 1201, 2)).to eq(32)
  end

  it "gives 16x value if is from same group 5" do
    expect(prize(2, 1205, 7)).to eq(32)
  end

  it "gives 16x value if is from same group 6" do
    expect(prize(2, 1205, 3)).to eq(0)
  end

  it "gives 16x value if is from same group 6" do
    expect(prize(2, 3405, 3)).to eq(0)
  end

  it "gives 16x value if is from same group 6" do
    expect(prize(2, 3405, 1206)).to eq(32)
  end

end