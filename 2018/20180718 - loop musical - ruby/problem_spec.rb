require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1089

describe "Loop Musical" do
  it "2 different magnitudes, 2 peaks" do
    magnitudes = [0, 1]
    expect(musical_loop(magnitudes)).to eq(2)
  end

  it "2 equal magnitudes, 0 peaks" do
    magnitudes = [0, 0]
    expect(musical_loop(magnitudes)).to eq(0)
  end
end
