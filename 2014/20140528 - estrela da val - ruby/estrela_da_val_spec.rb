require './estrela_da_val'

describe 'estrela_da_val' do
  it '3 pontos' do
    expect(estrela_da_val(3)).to eq(1)
  end

  it '5 pontos' do
    expect(estrela_da_val(5)).to eq(2)
  end

  it '6 pontos' do
    expect(estrela_da_val(6)).to eq(1)
  end

  it '7 pontos' do
    expect(estrela_da_val(7)).to eq(3)
  end

  it '8 pontos' do
    expect(estrela_da_val(8)).to eq(2)
  end

  it '9 pontos' do
    expect(estrela_da_val(9)).to eq(3)
  end

  it '10 pontos' do
    expect(estrela_da_val(10)).to eq(2)
  end

  it '11 pontos' do
    expect(estrela_da_val(11)).to eq(5)
  end

  it '12 pontos' do
    expect(estrela_da_val(12)).to eq(2)
  end

  it '13 pontos' do
    expect(estrela_da_val(13)).to eq(6)
  end

  it '18 pontos' do
    expect(estrela_da_val(18)).to eq(3)
  end

end
