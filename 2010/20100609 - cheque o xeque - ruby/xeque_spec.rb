require 'xeque'

describe 'Xeque' do

  it 'peao branco na 4,5 e rei preto na 5,4 deve retornar peão' do
    rei = Peca.new(
      :tipo => :rei,
      :linha => 5,
      :coluna => 4,
      :cor => :preto
    )
    peao = Peca.new(
      :tipo => :peao,
      :linha => 4,
      :coluna => 5,
      :cor => :branco
    )
    jogo = Jogo.new([rei, peao])
    jogo.atacantes.should == peao
  end

  it 'peao branco na 5,5 e rei preto na 6,4 deve retornar peão' do
    rei = Peca.new(
      :tipo => :rei,
      :linha => 6,
      :coluna => 4,
      :cor => :preto
    )
    peao = Peca.new(
      :tipo => :peao,
      :linha => 5,
      :coluna => 5,
      :cor => :branco
    )
    jogo = Jogo.new([rei, peao])
    jogo.atacantes.should == peao
  end

  it 'peao branco na 3,5 e rei preto na 6,4 deve retornar nada' do
    rei = Peca.new(
      :tipo => :rei,
      :linha => 6,
      :coluna => 4,
      :cor => :preto
    )
    peao = Peca.new(
      :tipo => :peao,
      :linha => 3,
      :coluna => 5,
      :cor => :branco
    )
    jogo = Jogo.new([rei, peao])
    jogo.atacantes.should == nil
  end

  it 'peao branco na 2,4 e rei preto na 6,4 deve retornar nada' do
    rei = Peca.new(
      :tipo => :rei,
      :linha => 6,
      :coluna => 4,
      :cor => :preto
    )
    peao = Peca.new(
      :tipo => :peao,
      :linha => 2,
      :coluna => 4,
      :cor => :branco
    )
    jogo = Jogo.new([rei, peao])
    jogo.atacantes.should == nil
  end

end

