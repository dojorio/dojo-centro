require_relative 'problem'

describe "problem" do
  it "um" do
    valor = 1
    expect(contaletras(valor)).to eq(2)
  end

  it "dois" do
    valor = 2
    expect(contaletras(valor)).to eq(6)
  end

  it "três" do
    valor = 3
    expect(contaletras(valor)).to eq(10)
  end

  it "quatro" do
    valor = 4
    expect(contaletras(valor)).to eq(16)
  end
end
