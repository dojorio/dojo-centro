require 'validador'

describe 'Validador' do
  it 'deve validar expressao com o número 7' do
    validar('7').should be_true
  end

  it 'deve validar expressao X falso' do
    validar('X').should be_false
  end

  it 'deve validar expressao que possui numero entre 0 e 9' do
    validar('9').should be_true
    validar('5').should be_true
  end

  it 'deve validar expressao com número 99' do
    validar('99').should be_false
  end

  it 'deve validar expressao com número -9' do
    validar('-9').should be_true
  end

  it 'deve validar expressao somente com números entre 0 e 9 precedidos de "-"' do
    validar('-5').should be_true
    validar('-0').should be_true
  end

  it 'deve validar expressao somente com números entre 0 e 9 precedidos de "+"' do
    validar('+5').should be_true
  end
end

