require_relative 'animal_game'

describe "Animal game" do
  it "gives zero if no combination is found" do
    expect(prize(1, 1234, 0)).to eq(0)
  end

  it "gives 16x value if is from same group" do
    expect(prize(1, 1299, 0)).to eq(16)
  end
end