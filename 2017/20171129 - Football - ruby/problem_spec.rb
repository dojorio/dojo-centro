require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1495

describe "Football" do
  it "purchase 1 goal 1 loss" do
    goals = 1
    games = [[0, 1]]

    expect(football(goals, games)).to eq(1)
  end
  it "purchase 1 goal 1 draw" do
    goals = 1
    games = [[1, 1]]

    expect(football(goals, games)).to eq(3)
  end
  it "purchase 1 goal " do
    goals = 1
    games = [[1, 2]]

    expect(football(goals, games)).to eq(1)
  end

end
