require './roman.rb'

describe "A roman number" do 
  it "represents 1 as I" do
    expect(to_roman(1)).to eq("I")
  end

  it "represents 5 as V" do
    expect(to_roman(5)).to eq("V")
  end

  it "represents 10 as X" do
    expect(to_roman(10)).to eq("X")
  end

  it "represents 50 as L" do
    expect(to_roman(50)).to eq("L")
  end

  it "represents 100 as C" do
    expect(to_roman(100)).to eq("C")
  end

  it "represents 500 as D" do
    expect(to_roman(500)).to eq("D")
  end

  it "represents 1000 as M" do
    expect(to_roman(1000)).to eq("M")
  end

  it "represents 2 as II" do
    expect(to_roman(2)).to eq("II")
  end

  it "represents 3 as III" do
    expect(to_roman(3)).to eq("III")
  end

  it "represents 20 as XX" do
    expect(to_roman(20)).to eq("XX")
  end
end