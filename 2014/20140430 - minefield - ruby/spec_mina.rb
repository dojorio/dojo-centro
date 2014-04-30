require './mina'

describe 'Mina' do
  it '2x2 e 1 mina' do
    tabuleiro = [
      '..',
      '.*'
    ]
    expect(mina(tabuleiro)).to eq(3)
  end

  it '2x2 e 2 minas' do
    tabuleiro = [
      '*.',
      '.*'
    ]
    expect(mina(tabuleiro)).to eq(2)
  end

  it '2x2 e 2 minas mas diferente' do
    tabuleiro = [
      '.*',
      '.*'
    ]
    expect(mina(tabuleiro)).to eq(2)
  end

  it '2x2 sem mina' do
    tabuleiro = [
      '..',
      '..'
    ]
    expect(mina(tabuleiro)).to eq(1)
  end
end