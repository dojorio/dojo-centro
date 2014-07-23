require './velas'

describe "Velas" do
  it 'duas velas exatas' do
    idades = [5,5]
    velas  = [5,5]

    expect(particao_de_velas(idades, velas)).to eq(0)
  end
end