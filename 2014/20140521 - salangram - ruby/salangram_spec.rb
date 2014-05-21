require './salangram'

describe 'Salangram' do
  it 'salao 1mx1m 1 tabua 100cmx1m' do
    salao = [1, 1]
    largura = 100
    comprimentos = [1]

    expect(salangram(salao, largura, comprimentos)).to eq(1)
  end

  it 'salao 1mx2m 1 tauba 100cmx1m' do
    salao = [1, 2]
    largura = 100
    comprimentos = [1]

    expect(salangram(salao, largura, comprimentos)).to eq('impossivel')
  end

  it 'salao 2mx1m 1 tabua 100cmx1m' do
    salao = [2, 1]
    largura = 100
    comprimentos = [1]

    expect(salangram(salao, largura, comprimentos)).to eq('impossivel')
  end

  it 'salao 1mx2m 1 tabua 100cmx2m' do
    salao = [1, 2]
    largura = 100
    comprimentos = [2]

    expect(salangram(salao, largura, comprimentos)).to eq(1)
  end

  it 'salao 1mx1m 1 tabua 100cmx2m' do
    salao = [1, 1]
    largura = 100
    comprimentos = [2]

    expect(salangram(salao, largura, comprimentos)).to eq('impossivel')
  end

  it 'salao 1mx1m 2 tabua 100cmx2m 100cmx1m' do
    salao = [1, 1]
    largura = 100
    comprimentos = [2, 1]

    expect(salangram(salao, largura, comprimentos)).to eq(1)
  end

  it 'salao 1mx2m 2 tabua 100cmx1m' do
    salao = [1, 2]
    largura = 100
    comprimentos = [1, 1]

    expect(salangram(salao, largura, comprimentos)).to eq(2)
  end

  it 'salao 1mx2m 2 tabuas 100cmx2m' do
    salao = [1, 2]
    largura = 100
    comprimentos = [2, 2]

    expect(salangram(salao, largura, comprimentos)).to eq(1)
  end

  it 'salao 1mx2m 2 tabuas 100cmx1m 100cmx2m 100cmx3m' do
    salao = [1, 2]
    largura = 100
    comprimentos = [1, 2, 3]

    expect(salangram(salao, largura, comprimentos)).to eq(1)
  end

  it 'salao 1mx2m 2 tabuas 100cmx1m 100cmx1m 100cmx3m' do
    salao = [1, 2]
    largura = 100
    comprimentos = [1, 1, 3]

    expect(salangram(salao, largura, comprimentos)).to eq(2)
  end

  it 'salao 1mx2m 2 tabuas 100cmx3m 100cmx1m 100cmx1m' do
    salao = [1, 2]
    largura = 100
    comprimentos = [3, 1, 1]

    expect(salangram(salao, largura, comprimentos)).to eq(2)
  end

end