require './base.rb'

describe 'all your base' do
  it 'é 0 quando for vazio' do
    base('').should == 0
  end

  it 'é 1 quando for apenas um caractere' do
    base('a').should == 1
  end
end
