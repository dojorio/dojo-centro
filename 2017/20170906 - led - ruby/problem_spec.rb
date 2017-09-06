require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1168

describe "led" do
  it "is 2 for number 1" do
    expect(led(1)).to eq(2)
  end
  it "is 5 for number 2" do
    expect(led(2)).to eq(5)
  end
end
