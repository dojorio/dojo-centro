require './salangram'

describe 'Salangram' do
  it 'salao 1mx1m 1 tabua 100cmx1m' do
    salao = [1, 1]
    largura = 100
    comprimentos = [1]

    expect(salangram(salao, largura, comprimentos)).to eq(1)
  end
end