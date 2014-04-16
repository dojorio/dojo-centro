require './coelho'

describe "Coelho da Pascoa" do
  it 'um ovo perto' do
    ovos = [[0, 2]]
    velocidade = 2 # metro/minuto

    expect(coelho(ovos, velocidade)).to eq(1)
  end

  it 'um ovo longe' do
    ovos = [[0, 721]]
    velocidade = 2 # metro/minuto

    expect(coelho(ovos, velocidade)).to eq(0)
  end
end