require "./davinci.rb"

describe "da vinci's code" do
  it 'código vazio' do
    resultado = davinci([], '')
    resultado.should == ''
  end

  it 'código com 1 caractere e chave vazia deve resultar em mensagem vazia' do
    resultado = davinci([], 'A')
    resultado.should == ''
  end

  it 'código com 1 caractere e chave válida' do
    resultado = davinci([1], 'A')
    resultado.should == 'A'
  end

  it 'código com 2 caracteres e chave válida' do
    resultado = davinci([2, 1], 'BA')
    resultado.should == 'AB'
  end

  it 'código com 2 caracteres e chave válida, teste que o Carlos roubou' do
    resultado = davinci([2, 1], 'AB')
    resultado.should == 'BA'
  end

  it 'código com 2 caracteres e chave válida separado por espaço' do
    resultado = davinci([3, 1], 'AB')
    resultado.should == 'B A'
  end

  it 'código com 3 caracteres e chave válida separado por espaço' do
    resultado = davinci([3, 1, 8], 'ABC')
    resultado.should == 'B A C'
  end

  it 'código gigante' do
    resultado = davinci([1, 2], 'A,B')
    resultado.should == 'AB'
  end

end
