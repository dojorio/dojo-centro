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
end
