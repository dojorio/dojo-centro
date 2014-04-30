require './mina'

describe 'Mina' do
    it '2x2 e 1 mina' do
      tabuleiro = [
        '..',
        '.*'
      ]
      expect(mina(tabuleiro)).to eq(3)
    end
end