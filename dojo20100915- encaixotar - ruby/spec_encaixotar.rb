require 'encaixotar'

describe Encaixotador do

  before(:each) do
    @encaixotador = Encaixotador.new
  end

  it 'deve encaixotar as coisas [A] em uma caixa 1x1 "|A|"' do
    caixas = @encaixotador.encaixotar(['A'], 1, 1)
    caixas.should == '|A|'
  end

  it 'deve encaixotar as coisas [B] em uma caixa 1x1 "|B|"' do
    caixas = @encaixotador.encaixotar(['B'], 1, 1)
    caixas.should == '|B|'
  end

  it 'deve encaixotar as coisas [A, B] em duas caixas 1x1 "|A| |B|"' do
    caixas = @encaixotador.encaixotar(['A','B'], 1, 1)
    caixas.should == "|A|\n\n|B|"
  end

  it 'deve encaixotar as coisas [A, B] em uma caixa 1x2 "|AB|"' do
    caixas = @encaixotador.encaixotar(['A','B'], 1, 2)
    caixas.should == "|AB|"
  end

  it 'deve encaixotar as coisas [B, A] em uma caixa 1x2 "|BA|"' do
    caixas = @encaixotador.encaixotar(['B','A'], 1, 2)
    caixas.should == "|BA|"
  end

  it 'deve encaixotar as coisas [A, C, B] em uma caixa 1x3 "|ACB|"' do
    caixas = @encaixotador.encaixotar(['A','C','B'], 1, 3)
    caixas.should == "|ACB|"
  end

  it 'deve encaixotar as coisas [A, B] em uma caixa 1x3 "|ACB|"' do
    caixas = @encaixotador.encaixotar(['A','B'], 1, 3)
    caixas.should == "|AB-|"
  end

end

