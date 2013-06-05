require './pintar.rb'

describe 'pintar arvore' do

  it 'vazia' do
    arvore = nil
    expect(pintar arvore).to eq 0
  end

  it 'somente com raiz' do
    arvore = [10, nil, nil]
    expect(pintar arvore).to eq 10
  end

  it 'somente com o filho esquerdo' do
    arvore = [10,
                [2,
                  nil,
                  nil
                ],
                nil
             ]
    expect(pintar arvore).to eq 14
  end

  it 'somente com o filho direito' do
    arvore = [10,
                nil,
                [2,
                  nil,
                  nil
                ]
             ]
    expect(pintar arvore).to eq 14
  end
end
