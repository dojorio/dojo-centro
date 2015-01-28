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
end