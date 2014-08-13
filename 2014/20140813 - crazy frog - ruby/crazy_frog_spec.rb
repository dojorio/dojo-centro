require './crazy_frog'

describe "crazy_frog" do
  it '2m width no stones' do
    distance = 2
    stones = []

    expect(bigger_jump(distance, stones)).to eq(2)
  end

  it '3m width no stones' do
    distance = 3
    stones = []

    expect(bigger_jump(distance, stones)).to eq(3)
  end

  it '4m width no stones' do
    distance = 4
    stones = []

    expect(bigger_jump(distance, stones)).to eq(4)
  end
end