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

  it 'duas pessoas 8 e 3 anos com velas 2 e 9' do
    idades = [8,3]
    velas  = [2,9]

    expect(particao_de_velas(idades, velas)).to eq(2)
  end

  it 'uma pessoa 8 anos com velas 1 e 1' do
    idades = [8]
    velas  = [1,1]

    expect(particao_de_velas(idades, velas)).to eq(3)
  end

  it 'uma pessoa 8 anos com velas 1 e 0' do
    idades = [8]
    velas  = [1,0]

    expect(particao_de_velas(idades, velas)).to eq(2)
  end

  it 'uma pessoa 7 anos com velas 1 e 0' do
    idades = [7]
    velas  = [1,0]

    expect(particao_de_velas(idades, velas)).to eq(3)
  end

  it 'uma pessoa 7 anos com velas 0 e 1' do
    idades = [7]
    velas  = [0,1]

    expect(particao_de_velas(idades, velas)).to eq(3)
  end
end