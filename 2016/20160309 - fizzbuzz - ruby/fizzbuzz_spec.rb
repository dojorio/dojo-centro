# http://www.dojopuzzles.com/problemas/exibe/encontre-o-telefone
require_relative 'fizzbuzz'

describe 'Fizzbuzz' do
  it 'is Fizz for 3' do
    expect(fizzbuzz(3)).to eq('Fizz')
  end

  it 'is Buzz for 5' do
    expect(fizzbuzz(5)).to eq('Buzz')
  end
end