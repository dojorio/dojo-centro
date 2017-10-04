require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1025

describe "where is the marble?" do
  it "one marble one not found query" do
    marbles = [1]
    queries = [2]
    expect(where_is_the_marble(marbles, queries)).to eq([false])
  end

  it "one marble one found query" do
    marbles = [2]
    queries = [2]
    expect(where_is_the_marble(marbles, queries)).to eq([1])
  end
  it "two marbles one found query" do
    marbles = [1,2]
    queries = [2]
    expect(where_is_the_marble(marbles, queries)).to eq([2])
  end
  it "two marbles 2,5 one found query" do
    marbles = [2,5]
    queries = [2]
    expect(where_is_the_marble(marbles, queries)).to eq([1])
  end
  it "two marbles one found query inteligente" do
    marbles = [1,2]
    queries = [1]
    expect(where_is_the_marble(marbles, queries)).to eq([1])
  end
  it "one marbles[2] one not found query[1]" do
    marbles = [2]
    queries = [1]
    expect(where_is_the_marble(marbles, queries)).to eq([false])
  end
end

