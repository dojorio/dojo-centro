require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1495

describe "Football" do
  it "1 goal 1 loss" do
  	goals = 1
  	games = [[0, 1]]

    expect(football(goals, games)).to eq(1)
  end
end
