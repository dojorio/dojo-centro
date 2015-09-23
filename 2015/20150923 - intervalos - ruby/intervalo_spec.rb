require './intervalo'

describe "Intervalos" do
  it { expect(intervalos([1])).to eq(["1"]) }
  it { expect(intervalos([2])).to eq(["2"]) }
  it { expect(intervalos([3])).to eq(["3"]) }

  it { expect(intervalos([1, 3])).to eq(["1", "3"]) }
  it { expect(intervalos([1, 4])).to eq(["1", "4"]) }
  it { expect(intervalos([2, 4])).to eq(["2", "4"]) }

  it { expect(intervalos([1, 2])).to eq(["1-2"]) }
  it { expect(intervalos([2, 3])).to eq(["2-3"]) }
  it { expect(intervalos([3, 4])).to eq(["3-4"]) }
 
  it { expect(intervalos([1, 2, 4])).to eq(["1-2", "4"]) }
  it { expect(intervalos([2, 3, 5])).to eq(["2-3", "5"]) }
  it { expect(intervalos([3, 4, 6])).to eq(["3-4", "6"]) }
  it { expect(intervalos([3, 5, 6])).to eq(["3", "5-6"]) }
  it { expect(intervalos([1, 3, 5])).to eq(["1", "3", "5"]) }
  it { expect(intervalos([1, 2, 3])).to eq(["1-3"]) }
  it { expect(intervalos([2, 3, 4])).to eq(["2-4"]) }

end