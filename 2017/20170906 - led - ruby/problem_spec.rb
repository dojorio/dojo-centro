require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1168

describe "led" do
  it "is 2 for number 1" do
    expect(led(1)).to eq(2)
  end
  it "is 5 for number 2" do
    expect(led(2)).to eq(5)
  end
  it "is 5 for number 3" do
    expect(led(3)).to eq(5)
  end
  it "is 4 for number 4" do
    expect(led(4)).to eq(4)
  end
  it "is 5 for number 5" do
    expect(led(5)).to eq(5)
  end
  it "is 6 for number 6" do
    expect(led(6)).to eq(6)
  end
  it "is 3 for number 7" do
    expect(led(7)).to eq(3)
  end
  it "is 7 for number 8" do
    expect(led(8)).to eq(7)
  end
  it "is 6 for number 9" do
    expect(led(9)).to eq(6)
  end
  it "is 6 for number 0" do
    expect(led(0)).to eq(6)
  end
  it "is 4 for number 11" do
    expect(led(11)).to eq(4)
  end
  it "is 7 for number 12" do
    expect(led(12)).to eq(7)
  end
end
