# http://www.dojopuzzles.com/problemas/exibe/caixa-eletronico/
require './caixa_eletronico'

describe 'Caixa Eletronico' do
  it 'sacar 10 reais' do
    expect(sacar(10)).to eq([10])
  end

  it 'sacar 20 reais' do
    expect(sacar(20)).to eq([20])
  end

  it 'sacar 50 reais' do
    expect(sacar(50)).to eq([50])
  end
end