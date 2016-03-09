# http://www.dojopuzzles.com/problemas/exibe/encontre-o-telefone
require_relative 'fizzbuzz'

describe 'Fizzbuzz' do
  it 'is Fizz for 3' do
    expect(fizzbuzz(3)).to eq('Fizz')
  end
 
  it 'is Fizz for 6' do
    expect(fizzbuzz(6)).to eq('Fizz')
  end

  it 'is Fizz for 9' do
    expect(fizzbuzz(9)).to eq('Fizz')
  end

  it 'is Buzz for 5' do
    expect(fizzbuzz(5)).to eq('Buzz')
  end

  it 'is Buzz for 10' do
    expect(fizzbuzz(10)).to eq('Buzz')
  end

  it 'is Buzz for 15' do
    expect(fizzbuzz(15)).to eq('FizzBuzz')
  end
  
  it 'is 1 for 1' do
    expect(fizzbuzz(1)).to eq(1)
  end
end
