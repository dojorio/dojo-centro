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

  describe 'em tabuleiro 3x2' do
    it 'uma mina no cantinho' do
      tabuleiro = [
        '..',
        '..',
        '.*'
      ]
      expect(mina(tabuleiro)).to eq(2)
    end

    it 'uma mina no ~meio~' do
      tabuleiro = [
        '..',
        '.*',
        '..'
      ]
      expect(mina(tabuleiro)).to eq(5)
    end
  end

  describe 'em tabuleiro 2x3' do
    it 'uma mina no cantinho' do
      tabuleiro = [
        '...',
        '..*'
      ]
      expect(mina(tabuleiro)).to eq(2)
    end

    it 'uma mina outro cantinho' do
      tabuleiro = [
        '...',
        '*..'
      ]
      expect(mina(tabuleiro)).to eq(2)
    end
  end

end