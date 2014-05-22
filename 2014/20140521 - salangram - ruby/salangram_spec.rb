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

  it 'salao 1mx3m 3 tabuas 100cmx1m 100cmx1m 100cmx2m' do
    salao = [1, 3]
    largura = 100
    comprimentos = [1, 1, 2]

    expect(salangram(salao, largura, comprimentos)).to eq(2)
  end

  it 'salao 1mx3m 3 tabuas 100cmx2m 100cmx1m 100cmx1m ' do
    salao = [1, 3]
    largura = 100
    comprimentos = [2, 1, 1]

    expect(salangram(salao, largura, comprimentos)).to eq(2)
  end

  it 'salao 1mx3m 3 tabuas 100cmx1m 100cmx1m 100cmx7m ' do
    salao = [1, 2]
    largura = 100
    comprimentos = [1, 1, 7]

    expect(salangram(salao, largura, comprimentos)).to eq(2)
  end

  it 'salao 1mx6m 4 tabuas 100cmx5m 100cmx2m 100cmx2m 100cmx2m' do
    salao = [1, 6]
    largura = 100
    comprimentos = [2, 2, 2, 5]

    expect(salangram(salao, largura, comprimentos)).to eq(3)
  end

  it 'salao 2mx2m 2 tabuas 100cmx2m 100cmx2m' do
    salao = [2, 2]
    largura = 100
    comprimentos = [2, 2]

    expect(salangram(salao, largura, comprimentos)).to eq(2)
  end

  it 'salao 2mx3m 3 tabuas 100cmx2m 100cmx2m 100cmx2m' do
    salao = [2, 3]
    largura = 100
    comprimentos = [2, 2, 2]

    expect(salangram(salao, largura, comprimentos)).to eq(3)
  end


end