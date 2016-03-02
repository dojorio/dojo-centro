#https://www.urionlinejudge.com.br/judge/en/problems/view/1750
require_relative 'help_cupid'

describe 'Help Cupid' do
  it 'two people, same timezone' do
    expect(help_cupid([0, 0])).to eq(0)
  end

  it 'two people, side by side timezone' do
    expect(help_cupid([0, 1])).to eq(1)
  end

  it 'two people, side by side timezone 2' do
    expect(help_cupid([1, 0])).to eq(1)
  end

  it 'two people, side by side timezone 3' do
    expect(help_cupid([1, 2])).to eq(1)
  end

  it 'two people, far away timezone' do
    expect(help_cupid([1, 3])).to eq(2)
  end

  it 'two couple, each with same place' do
    expect(help_cupid([0, 0, 1, 1])).to eq(0)
  end

  it 'two couple, each with same place 2' do
    expect(help_cupid([1, 0, 1, 0])).to eq(0)
  end

  it 'two couple, three in the same place' do
    expect(help_cupid([0, 0, 0, 1])).to eq(1)
  end

  it 'two couple, three in the same place 2' do
    expect(help_cupid([0, 0, 1, 0])).to eq(1)
  end

  it 'two couple, three different places' do
    expect(help_cupid([0, 1, 2, 2])).to eq(1)
  end

  it 'two couple, three different places 2' do
    expect(help_cupid([-11, 11, 12, 12])).to eq(2)
  end

  it 'two couple, three different places 3' do
    expect(help_cupid([-11, -11, -10, 12])).to eq(2)
  end

  it 'two couple, three different places 4' do
    expect(help_cupid([-11, 0, 0, 12])).to eq(1)
  end
end