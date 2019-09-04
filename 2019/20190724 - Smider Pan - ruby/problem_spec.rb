require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/2943

describe "Smider Pan" do
  it "buildings 1" do
    buildings = [1]
    expect(smider_pan(buildings)).to eq(2)
  end

  it "buildings 1, 2" do
    buildings = [1, 2]
    expect(smider_pan(buildings)).to eq(3)
  end

  it "buildings 2, 1" do
    buildings = [2, 1]
    expect(smider_pan(buildings)).to eq(3)
  end

  it "buildings 1, 1" do
    buildings = [1, 1]
    expect(smider_pan(buildings)).to eq(2)
  end

  it "buildings 1, 2, 3" do
    buildings = [1, 2, 3]
    expect(smider_pan(buildings)).to eq(4)
  end

  it "buildings 2, 1, 3" do
    buildings = [2, 1, 3]
    expect(smider_pan(buildings)).to eq(3)
  end

  it "buildings 1, 1, 1" do
    buildings = [1, 1, 1]
    expect(smider_pan(buildings)).to eq(2)
  end

  it "buildings 3, 2, 1" do
    buildings = [3, 2, 1]
    expect(smider_pan(buildings)).to eq(4)
  end

  it "buildings 1, 2, 3, 4" do
    buildings = [1, 2, 3, 4]
    expect(smider_pan(buildings)).to eq(5)
  end

  it "buildings 2, 1, 3, 4" do
    buildings = [2, 1, 3, 4]
    expect(smider_pan(buildings)).to eq(4)
  end

  it "buildings 3, 1, 2, 4" do
    buildings = [3, 1, 2, 4]
    expect(smider_pan(buildings)).to eq(4)
  end

  it "buildings 5, 3, 9, 4, 6, 3, 7" do
    buildings = [5, 3, 9, 4, 6, 3, 7]
    expect(smider_pan(buildings)).to eq(5)
  end

  it "buildings 5, 10, 1, 2, 3, 4, 5" do
    buildings = [5, 10, 1, 2, 3, 4, 5]
    expect(smider_pan(buildings)).to eq(6)
  end


end
