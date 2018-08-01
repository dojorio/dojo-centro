require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/2821

describe "Cards Distribution" do
  it "2 cards, 1 player" do
    cards = ['A', 'A']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(2)
  end

  it "3 cards, 1 player" do
    cards = ['A', 'A', 'A']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(3)
  end

  it "2 other cards, 1 player" do
    cards = ['A', '2']
    player_quantity = 1
    expect(max_sum(cards, player_quantity)).to eq(3)
  end
end
