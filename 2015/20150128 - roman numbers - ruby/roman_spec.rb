require './roman.rb'

describe "A roman number" do 
  it "represents 1 as I" do
    expect(to_roman(1)).to eq("I")
  end

  it "represents 5 as V" do
    expect(to_roman(5)).to eq("V")
  end
end