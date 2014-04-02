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

    it 'tres ruas mesmo tamanho' do
      ruas = [[0, 1, 1], [0, 2, 1], [1, 2, 1]]
      expect(apagao(ruas)).to eq(1) 
    end

    it 'tres ruas uma maior' do
      ruas = [[0, 1, 1], [0, 2, 1], [1, 2, 2]]
      expect(apagao(ruas)).to eq(2)
    end

    it 'quatro ruas mesmo tamanho' do
      ruas = [[0, 1, 1], [0, 2, 1], [1, 2, 1],[0, 2, 1]]
      expect(apagao(ruas)).to eq(2)
    end
  end
end