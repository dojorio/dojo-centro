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

    it '1 mina outro canto' do
      tabuleiro = [
        '..',
        '*.'
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

    it 'uma mina no cantinho de cima' do
      tabuleiro = [
        '..*',
        '...'
      ]
      expect(mina(tabuleiro)).to eq(2)
    end
  end
end

describe 'Tenta com a mina' do
  describe '2x2' do
    it '1 mina' do
      tabuleiro = [
          '.*',
          '..'
      ]
      esperado = [
          '1*',
          '..'
      ]
      click!(tabuleiro, 0, 0)
      
      expect(tabuleiro).to eq(esperado)
    end

    it '2 minas' do
      tabuleiro = [
          '.*',
          '.*'
      ]
      esperado = [
          '2*',
          '.*'
      ]
      click!(tabuleiro, 0, 0)
      
      expect(tabuleiro).to eq(esperado)
    end
  end

  describe '3x2' do
    it '2 minas separadas' do
      tabuleiro = [
          '.*',
          '..',
          '.*'
      ]
      esperado = [
          '1*',
          '..',
          '.*'
      ]
      click!(tabuleiro, 0, 0)
      
      expect(tabuleiro).to eq(esperado)
    end

    it '1 mina no cantinho' do
      tabuleiro = [
          '..',
          '..',
          '.*'
      ]
      esperado = [
          '00',
          '11',
          '.*'
      ]
      click!(tabuleiro, 0, 0)
      
      expect(tabuleiro).to eq(esperado)
    end

    it '1 mina no cantinho e um rapaz se aproximando' do
      tabuleiro = [
          '..',
          '..',
          '.*'
      ]
      esperado = [
          '..',
          '..',
          '1*'
      ]
      click!(tabuleiro, 2, 0)
      
      expect(tabuleiro).to eq(esperado)
    end
  end
end

describe 'conta_mina' do
  it 'com 1 mina' do
    tabuleiro = [
      '.*',
      '..'
    ]

    expect(conta_mina(tabuleiro, 0, 0)).to eq(1)
  end

  it 'com 2 minas com uma de bobs' do
    tabuleiro = [
      '.*',
      '*.',
      '.*'
    ]
    
    expect(conta_mina(tabuleiro, 0, 0)).to eq(2)
  end
end


