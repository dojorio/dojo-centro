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

  it 'um ovo longe com alta velocidade' do
    ovos = [[0, 721]]
    velocidade = 20 # metro/minuto

    expect(coelho(ovos, velocidade)).to eq(1)
  end

  it 'dois ovos perto' do
    ovos = [[0, 2],[0, 4]]
    velocidade = 5 # metro/minuto

    expect(coelho(ovos, velocidade)).to eq(2)
  end

  it 'dois ovos em outra posicao' do
    ovos = [[0,1400], [0,4]]
    velocidade = 2

    expect(coelho(ovos, velocidade)).to eq(1)
  end
end