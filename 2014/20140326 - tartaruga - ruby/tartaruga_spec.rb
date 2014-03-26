require './tartaruga'

describe 'Aquiles' do
  it 'pega uma tartaruga' do
    tratador = [1, 1]
    tartaruga = [2, 1, 'D']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(1)
  end

  it 'pega uma tartaruga mais longe' do
    tratador = [1, 1]
    tartaruga = [3, 1, 'D']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(2)
  end

  it 'pega uma tartaruga na mesma coluna indo pra cima' do
    tratador = [1, 1]
    tartaruga = [1, 2, 'C']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(1)
  end

  it 'pega uma tartaruga na mesma linha indo pra cima' do
    tratador = [1, 1]
    tartaruga = [2, 1, 'C']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(1)
  end

  it 'pega uma tartaruga chegando na mesma linha indo pra direita' do
    tratador = [2, 1]
    tartaruga = [1, 1, 'D']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(1)
  end

  it 'pega uma tartaruga chegando na mesma linha indo pra direita mais longe' do
    tratador = [3, 1]
    tartaruga = [1, 1, 'D']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(1)
  end

  it 'pega uma tartaruga chegando na mesma linha indo pra direita ainda mais longe' do
    tratador = [4, 1]
    tartaruga = [1, 1, 'D']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(1)
  end

  it 'pega uma tartaruga chegando na mesma linha indo pra direita ainda mais longe do que nenhuma tartaruga jamais foi' do
    tratador = [5, 1]
    tartaruga = [1, 1, 'D']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(2)
  end

  it 'pega uma tartaruga para cima' do
    tratador = [1, 5]
    tartaruga = [1, 1, 'C']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(2)
  end

  it 'pega uma tartaruga para direita' do
    tratador = [1, 5]
    tartaruga = [1, 1, 'D']
    expect(pega_tartaruga(tratador, tartaruga)).to eq(4)
  end
end