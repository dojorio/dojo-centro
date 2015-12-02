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
end