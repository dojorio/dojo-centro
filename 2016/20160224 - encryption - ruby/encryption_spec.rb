#https://www.urionlinejudge.com.br/judge/en/problems/view/1024
require_relative 'encryption'

describe 'Encryption' do
  it 'one character "a"' do
    expect(encrypt('a')).to eq('c')
  end

  it 'one character "1"' do
    expect(encrypt('1')).to eq('0')
  end  

  it 'one character "."' do
    expect(encrypt('.')).to eq('-')
  end

  it 'one character "d"' do
    expect(encrypt('d')).to eq('f')
  end

  it 'one character "A"' do
    expect(encrypt('A')).to eq('C')
  end

  it 'one character "|"' do
    expect(encrypt('|')).to eq('{')
  end
end