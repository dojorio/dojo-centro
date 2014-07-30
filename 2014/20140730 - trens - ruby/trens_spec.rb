require './trens'

describe "Trens" do
  it "origin A destination B max_distance 5 return 1" do
    expect(routes_number(['AB5'], 'A', 'B', 5)).to eq(1)
  end
end