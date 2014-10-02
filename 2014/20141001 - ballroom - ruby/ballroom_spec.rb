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

  it '1x2 with 1 plank 1m' do
    expect(ballroom(1, 2, [1])).to eq("impossivel")
  end

  it '2x1 with 1 plank 1m' do
    expect(ballroom(2, 1, [1])).to eq("impossivel")
  end

  it '2x1 with 1 plank 3m' do
    expect(ballroom(2, 1, [3])).to eq("impossivel")
  end

  it '1x4 with 2 planks 1m 1m' do
    expect(ballroom(1, 4, [1, 1])).to eq("impossivel")
  end

  it '1x2 with 2 planks 1m 3m' do
    expect(ballroom(1, 2, [1, 3])).to eq("impossivel")
  end

  it '1x3 with 3 planks 1m 2m 2m' do
    expect(ballroom(1, 3, [1, 2, 2])).to eq(2)
  end

  it '1x3 with 3 planks 2m 2m 1m' do
    expect(ballroom(1, 3, [2, 2, 1])).to eq(2)
  end

  it '1x4 with 3 plank 2m 2m 1m' do
    expect(ballroom(1, 4, [2, 2, 1])).to eq(2)
  end

  it '1x5 with 3 planks 2m 3m 4m' do
    expect(ballroom(1, 5, [2, 3, 4])).to eq(2)
  end

  it '1x8 with 4 planks 4m 3m 2m 2m' do
    expect(ballroom(1, 8, [4, 3, 2, 2])).to eq(3)
  end
end