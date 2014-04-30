require './mina'

describe 'Mina' do
  describe 'em tabuleiro 2x2' do
    it '1 mina' do
      tabuleiro = [
        '..',
        '.*'
      ]
      expect(mina(tabuleiro)).to eq(3)
    end

    it '2 minas' do
      tabuleiro = [
        '*.',
        '.*'
      ]
      expect(mina(tabuleiro)).to eq(2)
    end

    it '2 minas mas diferente' do
      tabuleiro = [
        '.*',
        '.*'
      ]
      expect(mina(tabuleiro)).to eq(2)
    end

    it 'sem mina' do
      tabuleiro = [
        '..',
        '..'
      ]
      expect(mina(tabuleiro)).to eq(1)
    end
  end
end