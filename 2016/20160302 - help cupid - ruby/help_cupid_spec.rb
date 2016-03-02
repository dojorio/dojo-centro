#https://www.urionlinejudge.com.br/judge/en/problems/view/1750
require_relative 'help_cupid'

describe 'Help Cupid' do
  it 'two people, same timezone' do
    expect(help_cupid([0,0])).to eq(0)
  end

  it 'two people, side by side timezone' do
    expect(help_cupid([0,1])).to eq(1)
  end

  it 'two people, side by side timezone 2' do
    expect(help_cupid([1,0])).to eq(1)
  end

  it 'two people, side by side timezone 3' do
    expect(help_cupid([1,2])).to eq(1)
  end
end