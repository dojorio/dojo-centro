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

  it '3 7' do
    expect(houses(3, 7)).to eq 5
  end

  it '10 12' do
    expect(houses(10, 12)).to eq 2
  end

  it '1 30' do
    expect(houses(1, 30)).to eq 28
  end

  it '100 121' do
    expect(houses(100, 121)).to eq 9
  end

  it '100 123' do
    expect(houses(100, 123)).to eq 10
  end

  it '1 5000' do
    expect(houses(1, 500000000)).to eq 2754
  end
end