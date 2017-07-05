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

  it "fiho igual ao pai 2" do
    lista = ['A', 'C', 'C']
    expect(teste_de_dna(lista)).to eq('Pai 2')
  end

  it "fiho igual ao pai 1 C" do
    lista = ['C', 'A', 'C']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end

  it "fiho cadim" do
    lista = ['C', 'C', 'C']
    expect(teste_de_dna(lista)).to eq('cadim')
  
  end 

  it "fiho Pai 1" do
    lista = ['AC', 'GT', 'AA']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end




end





