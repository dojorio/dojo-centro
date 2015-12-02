require './telefone'

describe "Telefone" do
  it "is 2 for A" do
    expect(telefone_de('A')).to eq('2')
  end

  it "is 3 for D" do
    expect(telefone_de('D')).to eq('3')
  end

  it "is 3 for E" do
    expect(telefone_de('E')).to eq('3')
  end

    it "is 3 for F" do
    expect(telefone_de('F')).to eq('3')
  end

    it "is 4 for G" do
    expect(telefone_de('G')).to eq('4')
  end

     it "is 4 for H" do
    expect(telefone_de('H')).to eq('4')
  end

    it "is 4 for I" do
    expect(telefone_de('I')).to eq('4')
  end
end