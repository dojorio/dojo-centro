require './poker'

RSpec.describe 'poker' do
  it 'identifica a maior carta de uma mao' do
    mao = ['2H', '3H', '7C', '9D', '6S']
    expect(maior_carta(mao)).to eq('9D')
  end
end