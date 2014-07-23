require './velas'

describe "Velas" do
  it 'duas velas exatas' do
    idades = [5,5]
    velas  = [5,5]

    expect(particao_de_velas(idades, velas)).to eq(0)
  end

  it 'duas velas nao exatas por 1' do
    idades = [5,5]
    velas  = [4,4]

    expect(particao_de_velas(idades, velas)).to eq(2)
  end


  it 'duas idades exatas com velas distintas' do
    idades = [5,5]
    velas  = [2,4]

    expect(particao_de_velas(idades, velas)).to eq(4)
  end

  it 'duas idades distintas com 2 velas distintas' do
    idades = [5,3]
    velas  = [1,4]

    expect(particao_de_velas(idades, velas)).to eq(3)
  end

  it 'duas idades distintas com 2 velas distintas invertidas' do
    idades = [5,3]
    velas  = [4,1]

    expect(particao_de_velas(idades, velas)).to eq(3)
  end
end