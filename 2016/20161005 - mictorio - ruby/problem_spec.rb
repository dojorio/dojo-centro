require_relative 'problem'

describe "Urinal" do
  it "one empty urinal" do
    pissers = '.'
    expect(urinal(pissers)).to eq(1)
  end

  it "one occupied urinal" do
    pissers = '*'
    expect(urinal(pissers)).to eq(0)
  end

  it "two empty urinals" do
    pissers = '..'
    expect(urinal(pissers)).to eq(1)
  end

  it "three urinals with 1 pisser on the edge" do
    pissers = '*..'
    expect(urinal(pissers)).to eq(1)
  end

  it "three urinals with 1 pisser on the other edge" do
    pissers = '..*'
    expect(urinal(pissers)).to eq(1)
  end

  it "four empty urinals" do
    pissers = '....'
    expect(urinal(pissers)).to eq(2)
  end

  it "four urinals with pissers on the edges" do
    pissers = '*..*'
    expect(urinal(pissers)).to eq(0)
  end

  it "five urinals with pissers on the edges" do
    pissers = '*...*'
    expect(urinal(pissers)).to eq(1)
  end

  it "three urinals empty" do
    pissers = '...'
    expect(urinal(pissers)).to eq(2)
  end
  
  it "three urinals with a bastard" do
    pissers = '.*.'
    expect(urinal(pissers)).to eq(0)
  end

  it "five urinals with positions 1 and 3" do
    pissers = '*.*..'
    expect(urinal(pissers)).to eq(1)
  end

  it "five urinals with positions 1 and 4" do
    pissers = '*..*.'
    expect(urinal(pissers)).to eq(0)
  end

  it "five urinals with positions 2 and 5" do
    pissers = '.*..*'
    expect(urinal(pissers)).to eq(0)
  end

  it "five urinals with positions 2 and 4" do
    pissers = '.*.*.'
    expect(urinal(pissers)).to eq(0)
  end

  it "six urinals with positions 2 and 5" do
    pissers = '.*..*.'
    expect(urinal(pissers)).to eq(0)
  end

end
