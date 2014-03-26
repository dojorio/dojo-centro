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

end