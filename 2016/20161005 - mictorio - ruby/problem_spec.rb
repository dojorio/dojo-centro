require_relative 'problem'

describe "Mictorio" do
  it "one empty mictorio" do
    bar = '.'
    expect(mictorio(bar)).to eq(1)
  end

  it "one occupied mictorio" do
    bar = '*'
    expect(mictorio(bar)).to eq(0)
  end
end
