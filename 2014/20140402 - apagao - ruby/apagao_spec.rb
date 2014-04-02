require './apagao'

describe "Apagão" do
  it 'dois pontos com uma rua' do
    ruas = [[0, 1, 1]]
    expect(apagao(ruas)).to eq(0)
  end

  context 'três pontos' do
    it 'duas ruas' do
      ruas = [[0, 1, 1], [0, 2, 1]]
      expect(apagao(ruas)).to eq(0)
    end
  end
end