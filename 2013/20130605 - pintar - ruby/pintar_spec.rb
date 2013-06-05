require './pintar.rb'

describe 'pintar arvore' do

  it 'vazia' do
    arvore = []
    expect(pintar arvore).to eq 0
  end

  it 'somente com raiz' do
    arvore = [10, [], []]
    expect(pintar arvore).to eq 10
  end

  it 'somente com o filho esquerdo' do
    arvore = [10,
                [2, [], []],
                []
             ]
    expect(pintar arvore).to eq 14
  end

  it 'somente com o filho direito' do
    arvore = [10,
                [],
                [2, [], []]
             ]
    expect(pintar arvore).to eq 14
  end


  it 'com dois filhos iguais' do
    arvore = [10,
                [2, [], []],
                [2, [], []]
             ]
    expect(pintar arvore).to eq 20
  end

end
