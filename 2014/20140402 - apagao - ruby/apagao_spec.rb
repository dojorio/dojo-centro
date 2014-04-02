require './apagao'

describe "Apagão" do
  context 'dois pontos' do
    it 'com uma rua' do
      ruas = [[0, 1, 1]]
      expect(apagao(ruas)).to eq(0)
    end

    it 'com duas ruas iguais' do
      ruas = [[0, 1, 1], [0, 1, 1]]
      expect(apagao(ruas)).to eq(1)
    end

    it 'com duas ruas diferentes' do
      ruas = [[0, 1, 1], [0, 1, 2]]
      expect(apagao(ruas)).to eq(2)
    end

    it 'com tres ruas iguais' do
      ruas = [[0, 1, 1], [1, 0, 1],[0, 1, 1]]
      expect(apagao(ruas)).to eq(2)
    end

    it 'com tres ruas diferentes' do
      ruas = [[0, 1, 1], [1, 0, 1],[0, 1, 2]]
      expect(apagao(ruas)).to eq(3)
    end
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

    it '2 pares de ruas' do
      ruas = [[0, 1 ,2], [0, 2, 2], [1, 2, 1], [2, 1, 1]]
      expect(apagao(ruas)).to eq(3)
    end
  end
end