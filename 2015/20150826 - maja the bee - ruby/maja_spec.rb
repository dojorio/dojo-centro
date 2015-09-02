require './maja'

describe "Maja" do
  it { expect(maja_coord(1)).to eq([0, 0])  }
  it { expect(maja_coord(2)).to eq([0, 1])  }
  it { expect(maja_coord(3)).to eq([-1, 1]) }
  it { expect(maja_coord(4)).to eq([-1, 0]) }
  it { expect(maja_coord(5)).to eq([0, -1]) }
  it { expect(maja_coord(6)).to eq([1, -1]) }
  it { expect(maja_coord(7)).to eq([1, 0]) }
  it { expect(maja_coord(8)).to eq([1, 1]) }
  it { expect(maja_coord(9)).to eq([0, 2]) }


end