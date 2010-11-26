require 'jogo'

  describe 'Jogo' do
    describe 'empate' do
      it 'deve empatar com papel e papel' do
        jogo('papel','papel').should be_eql :empate
      end

      it 'deve empatar se tesoura e tesoura' do
        jogo('tesoura','tesoura').should be_eql :empate
      end

       it 'deve empatar se pedra e pedra' do
        jogo('pedra','pedra').should be_eql :empate
      end
    end
  it 'papel deve vencer com papel e pedra' do
    jogo('papel','pedra').should be_eql :papel
  end

  it 'papel deve vencer com pedra e papel' do
    jogo('pedra','papel').should be_eql :papel
  end

  it 'tesoura deve vencer com papel e tesoura' do
    jogo('papel','tesoura').should be_eql :tesoura
  end

  it 'tesoura deve vencer com papel e tesoura' do
    jogo('tesoura','papel').should be_eql :tesoura
  end

  it 'pedra deve vencer tesoura' do
    jogo('pedra','tesoura').should be_eql :pedra
  end

  it 'pedra deve vencer tesoura' do
    jogo('tesoura','pedra').should be_eql :pedra
  end

  it 'spock e lagarto devem retornar nulo' do
    jogo('lagarto','spock').should be_eql nil
  end

end

