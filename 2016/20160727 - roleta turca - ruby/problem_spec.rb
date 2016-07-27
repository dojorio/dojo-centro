#https://www.urionlinejudge.com.br/judge/en/problems/view/1485
require_relative 'problem'

describe "Turkish roulette" do
  it "test 1" do
    roulette = [0, 0, 0]
    balls = [0]
    expect(max_profit(roulette, balls)).to eq(0)
  end

  it "test 2" do
    roulette = [1, 0, 0]
    balls = [-1]
    expect(max_profit(roulette, balls)).to eq(1)
  end

  it "test 3" do
    roulette = [1, 1, 0]
    balls = [-1]
    expect(max_profit(roulette, balls)).to eq(2)
  end

  it "test 4" do
    roulette = [1, 0, 1]
    balls = [-1]
    expect(max_profit(roulette, balls)).to eq(2)
  end

  it "test 5" do
    roulette = [-1, 0, 1]
    balls = [-2]
    expect(max_profit(roulette, balls)).to eq(2)
  end

  it "test 6" do
    roulette = [-1, 1, 1]
    balls = [-2]
    expect(max_profit(roulette, balls)).to eq(4)
  end

  it "test 7" do
    roulette = [1, 1, 1]
    balls = [-2]
    expect(max_profit(roulette, balls)).to eq(4)
  end

  it "test 8" do
    roulette = [1, 1, 1]
    balls = [-1]
    expect(max_profit(roulette, balls)).to eq(2)
  end

  it "test 9" do
    roulette = [-1, -1, -1]
    balls = [-1]
    expect(max_profit(roulette, balls)).to eq(-2)
  end

  it "test 10" do
    roulette = [-1, -1, -1]
    balls = [-2]
    expect(max_profit(roulette, balls)).to eq(-4)
  end

  it "test 11" do
    roulette = [-1, -1, -1]
    balls = [2]
    expect(max_profit(roulette, balls)).to eq(4)
  end

  it "test 12" do
    roulette = [2, 0, 0]
    balls = [2]
    expect(max_profit(roulette, balls)).to eq(0)
  end

  it "test 13" do
    roulette = [2, 2, 0]
    balls = [2]
    expect(max_profit(roulette, balls)).to eq(-4)
  end


  it "test 14" do
    roulette = [2, 2, 2]
    balls = [2]
    expect(max_profit(roulette, balls)).to eq(-8)
  end
end



