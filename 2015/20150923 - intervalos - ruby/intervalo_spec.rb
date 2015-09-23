require './intervalo'

describe "Intervalos" do
  it { expect(intervalos([1])).to eq([[1]]) }
  it { expect(intervalos([2])).to eq([[2]]) }
  it { expect(intervalos([3])).to eq([[3]]) }
end