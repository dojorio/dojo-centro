require './ballroom'

describe 'Ballroom' do
  it '1x1 with 1 plank 1m' do
    expect(ballroom(1,1,[1])).to eq(1)
  end

  it '1x2 with 2 planks 1m' do
    expect(ballroom(1,2,[1,1])).to eq(2)
  end

  it '2x1 with 2 planks 1m' do
    expect(ballroom(2,1,[1,1])).to eq(2)
  end

  it '1x2 with 2 planks 1m 2m' do
    expect(ballroom(1, 2, [1, 2])).to eq(1)
  end

  it '1x2 with 2 planks 2m 1m' do
    expect(ballroom(1, 2, [2, 1])).to eq(1)
  end

  it '1x2 with 2 planks 42m 2m' do
    expect(ballroom(1, 2, [42, 2])).to eq(1)
  end

end