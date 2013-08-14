require './base.rb'

describe 'all your base' do
  it 'é 0 quando for vazio' do
    base('').should == 0
  end

  it 'é 1 quando for apenas um caractere' do
    base('a').should == 1
  end

  it 'é 3 quando for aa' do
    base('aa').should == 3
  end

  it 'é 3 quando for bb' do
    base('bb').should == 3
  end

  it 'é 3 quando for cc' do
    base('cc').should == 3
  end

  it 'é 7 quando for aaa' do
    base('aaa').should == 7
  end

  it 'é 15 quando for aaaa' do
    base('aaaa').should == 15
  end

  it 'é 2 quando for ab' do
    base('ab').should == 2
  end

  it 'é 2 quando for ba' do
    base('ba').should == 2
  end

  it 'é  quando for acc' do
    base('acc').should == 4
  end

  it 'é  quando for accc' do
    base('accc').should == 8
  end
end
