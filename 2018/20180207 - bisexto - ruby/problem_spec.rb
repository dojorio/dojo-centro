require_relative 'problem'

describe "bisexto" do
  it "2021 não é divisivel por 4" do
    expect(bisexto(2021)).to eq(false)
  end

  it "2000 é divisivel por 4 e por 100" do
    expect(bisexto(2000)).to eq(true)
  end

  
end
