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
end
