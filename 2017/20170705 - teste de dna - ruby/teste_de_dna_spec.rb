require_relative 'teste_de_dna'

describe "teste_de_dna" do
  it "fiho diferente dos 2" do
    lista = ['A', 'C', 'T']
    expect(teste_de_dna(lista)).to eq('cadim')
  end

  it "fiho igual ao pai 1" do
    lista = ['A', 'C', 'A']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end
end
