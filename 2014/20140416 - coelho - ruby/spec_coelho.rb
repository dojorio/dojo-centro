require './coelho'

describe "Coelho da Pascoa" do
  it 'um ovo perto' do
    ovos = [[0, 2]]
    velocidade = 2

    expect(coelho(ovos, velocidade)).to eq(1)
  end
end