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

  it "3 magnitudes, 2 peaks" do
  magnitudes = [1, 0, -1]
    expect(musical_loop(magnitudes)).to eq(2)
  end

  it "4 magnitudes, 2 peaks" do 
    magnitudes = [1, 0, -1, 0]
    expect(musical_loop(magnitudes)).to eq(2)
  end

  it "4 magnitudes, 2 peaks again" do 
    magnitudes = [0, 1, 2, 1]
    expect(musical_loop(magnitudes)).to eq(2)
  end

  it "4 magnitudes, 2 peaks again yet" do 
    magnitudes = [1, 0, 1, 2]
    expect(musical_loop(magnitudes)).to eq(2)
  end

  it "5 magnitudes, 4 peaks" do 
    magnitudes = [3,2,1,2,-1]
    expect(musical_loop(magnitudes)).to eq(4)
  end

  it "5 magnitudes, 2 peaks" do 
    magnitudes = [3,2,1,2,4]
    expect(musical_loop(magnitudes)).to eq(2)
  end  
end
