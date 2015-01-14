require './poker'

RSpec.describe 'poker' do
  it "identifica a maior carta da mao '2H', '3H', '7C', '9D', '6S'" do
    mao = ['2H', '3H', '7C', '9D', '6S']
    expect(maior_carta(mao)).to eq('9D')
  end

  it "identifica a maior carta da mao '2H', '3H', '7C', '8D', '6S'" do
    mao = ['2H', '3H', '7C', '8D', '6S']
    expect(maior_carta(mao)).to eq('8D')
  end

  it "identifica a maior carta da mao 'TH', '3H', '7C', '8D', '6S'" do
    mao = ['TH', '3H', '7C', '8D', '6S']
    expect(maior_carta(mao)).to eq('TH')
  end

  it "identifica a maior carta da mao 'TH', 'JH', '7C', '8D', '6S'" do
    mao = ['TH', 'JH', '7C', '8D', '6S']
    expect(maior_carta(mao)).to eq('JH')
  end

  it "identifica a maior carta da mao 'QH', 'JH', '7C', '8D', '6S'" do
    mao = ['QH', 'JH', '7C', '8D', '6S']
    expect(maior_carta(mao)).to eq('QH')
  end

  it "identifica a maior carta da mao 'JH', 'QH', 'KC', '8D', '6S'" do
    mao = ['JH', 'QH', '7C', '8D', '6S']
    expect(maior_carta(mao)).to eq('QH')
  end
end