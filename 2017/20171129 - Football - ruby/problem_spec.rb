require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1495

describe "Football" do
  it "1 goal 1 draw" do
    goals = 1
    games = [[0, 1]]

    expect(football(goals, games)).to eq(1)
  end

  it "1 goal 1 win" do
    goals = 1
    games = [[1, 1]]

    expect(football(goals, games)).to eq(3)
  end

  it "1 goal 2 draw" do
    goals = 1
    games = [[1, 2]]

    expect(football(goals, games)).to eq(1)
  end

  it "0 goal 0 loss " do
    goals = 0
    games = [[0, 1]]

    expect(football(goals, games)).to eq(0)
  end
end
