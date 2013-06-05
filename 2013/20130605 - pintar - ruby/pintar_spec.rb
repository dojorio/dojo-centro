require './pintar.rb'

describe 'pintar arvore' do
  it 'vazia' do
    arvore = []
    expect(pintar arvore).to eq 0
  end

  it 'somente com raiz' do
    arvore = [10]
    expect(pintar arvore).to eq 10
  end

end
