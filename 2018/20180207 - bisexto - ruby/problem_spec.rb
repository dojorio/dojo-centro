require_relative 'problem'

describe "bisexto" do
  it "é divisivel por 4" do
    ano = 2020
    expect(bisexto(ano)).to eq(true)
  end
end
