require './roman.rb'

describe "A roman number" do 
  it "represents 1 as I" do
    expect(to_roman(1)).to eq("I")
  end
end