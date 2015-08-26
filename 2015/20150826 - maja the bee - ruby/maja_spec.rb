require './maja'

describe "Maja" do
  it { expect(maja_coord(1)).to eq([0, 0]) }
  it { expect(maja_coord(2)).to eq([0, 1]) }
end