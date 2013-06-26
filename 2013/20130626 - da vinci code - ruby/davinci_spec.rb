require "./davinci.rb"

describe "da vinci's code" do
  it 'código vazio' do
    resultado = davinci([], '')
    resultado.should == ''
  end

  it 'código com um caractere e chave vazia deve resultar em mensagem vazia' do
    resultado = davinci([], 'A')
    resultado.should == ''
  end

  it 'código com um caractere e chave válida' do
    resultado = davinci([1], 'A')
    resultado.should == 'A'
  end


end
