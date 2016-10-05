require_relative 'problem'

describe "Urinal" do
  it "one empty urinal" do
    bar = '.'
    expect(urinal(bar)).to eq(1)
  end

  it "one occupied urinal" do
    bar = '*'
    expect(urinal(bar)).to eq(0)
  end

  it "two empty urinals" do
    bar = '..'
    expect(urinal(bar)).to eq(1)
  end

end
