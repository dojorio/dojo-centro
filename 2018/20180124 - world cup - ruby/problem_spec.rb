require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1414

describe "World Cup" do
  it "has no draws when no game was played" do
    matches = 0
    teams = {
    	Brasil: 0,
    	Australia: 0
    }
    world_cup = WorldCup.new(matches, teams)

    expect(world_cup.draws).to eq(0)
  end

  it "has one draws when everebody has one point and one game was played" do
    matches = 1
    teams = {
    	Brasil: 1,
    	Australia: 1
    }
    world_cup = WorldCup.new(matches, teams)

    expect(world_cup.draws).to eq(1)
  end
end
