require './digits'

describe 'Digits' do
  it '1 1' do
    expect(houses(1, 1)).to eq(1)
  end

  it '1 2' do
    expect(houses(1, 2)).to eq(2)
  end

  it '1 3' do
    expect(houses(1, 3)).to eq(3)
  end

  it '2 3' do
    expect(houses(2, 3)).to eq(2)
  end

  it '1 11' do
    expect(houses(1, 11)).to eq 10 
  end

  it '2 11' do
    expect(houses(2, 11)).to eq 9
  end

  it '3 11' do
    expect(houses(3, 11)).to eq 8
  end
end