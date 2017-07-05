require_relative 'teste_de_dna'

describe "teste_de_dna" do
  it "filho diferente dos 2" do
    lista = ['A', 'C', 'T']
    expect(teste_de_dna(lista)).to eq('cadim')
  end

  it "filho igual ao pai 1" do
    lista = ['A', 'C', 'A']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end

  it "filho igual ao pai 2" do
    lista = ['A', 'C', 'C']
    expect(teste_de_dna(lista)).to eq('Pai 2')
  end

  it "filho igual ao pai 1 C" do
    lista = ['C', 'A', 'C']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end

  it "filho cadim" do
    lista = ['C', 'C', 'C']
    expect(teste_de_dna(lista)).to eq('cadim')
  end

  it "filho Pai 1" do
    lista = ['AC', 'GT', 'AA']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end

  it "filho Pai 2" do
    lista = ['GT', 'AC', 'AA']
    expect(teste_de_dna(lista)).to eq('Pai 2')
  end

  it "filho Pai 1 por pontuacao" do
    lista = ['AA', 'AC', 'AA']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end

  it "filho Pai 2 por pontuacao" do
    lista = ['AA', 'CT', 'CA']
    expect(teste_de_dna(lista)).to eq('cadim')
  end

  it "filho Pai 2 por igual" do
    lista = ['AA', 'AT', 'AT']
    expect(teste_de_dna(lista)).to eq('Pai 2')
  end

  it "filho Pai 1 por igual" do
    lista = ['AG', 'GC', 'AT']
    expect(teste_de_dna(lista)).to eq('Pai 1')
  end

  
end
