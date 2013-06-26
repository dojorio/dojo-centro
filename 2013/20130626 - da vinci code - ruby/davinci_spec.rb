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
    resultado = davinci([2, 1], 'AB')
    resultado.should == 'BA'
  end


end
