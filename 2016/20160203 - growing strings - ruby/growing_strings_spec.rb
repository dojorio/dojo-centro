#https://www.urionlinejudge.com.br/judge/en/problems/view/1141
require_relative 'growing_strings'

describe "growing_strings" do
  it "1 string" do
    expect(growing_strings(['foo'])).to eq(1)
  end

  it "2 string" do
    expect(growing_strings(['foo', 'bar'])).to eq(1)
  end

  it "2 string with successors" do
    expect(growing_strings(['fo', 'foo'])).to eq(2)
  end
end
