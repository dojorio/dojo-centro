require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1089

describe "Loop Musical" do
  it "2 different magnitudes, 2 peaks" do
    magnitudes = [0, 1]
    expect(musical_loop(magnitudes)).to eq(2)
  end


  it "4 magnitudes, 4 peaks" do
    magnitudes = [1, 0, 1, 0]
    expect(musical_loop(magnitudes)).to eq(4)
  end

end
