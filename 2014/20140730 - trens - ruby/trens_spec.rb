require './trens'

describe "Trens" do
  it "origin A destination B max_distance 5 return 1" do
    expect(routes_number(['AB5'], 'A', 'B', 5)).to eq(1)
  end

  it "origin A destination B max_distance 5 return 0" do
    expect(routes_number(['AB6'], 'A', 'B', 5)).to eq(0)
  end

  it "origin A destination B max_distance 6 return 1" do
    expect(routes_number(['AB6'], 'A', 'B', 6)).to eq(1)
  end

end