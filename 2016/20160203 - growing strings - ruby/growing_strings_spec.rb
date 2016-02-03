#https://www.urionlinejudge.com.br/judge/en/problems/view/1141
require_relative 'growing_strings'

describe "growing_strings" do
  it "1 string" do
    expect(growing_strings(['foo'])).to eq(1)
  end

  it "2 strings" do
    expect(growing_strings(['foo', 'bar'])).to eq(1)
  end

  it "2 strings with successors" do
    expect(growing_strings(['fo', 'foo'])).to eq(2)
  end

  it "2 strings with successors reloaded" do
    expect(growing_strings(['foo', 'fo'])).to eq(2)
  end

  it "3 strings sequence" do
    expect(growing_strings(['f', 'fo', 'foo'])).to eq(3)
  end

  it "3 strings, sequence of 2" do
    expect(growing_strings(['b', 'fo', 'foo'])).to eq(2)
  end

  it "3 strings, other sequence of 2" do
    expect(growing_strings(['fo', 'foo', 'b'])).to eq(2)
  end

  it "3 strings yet other sequence of 2" do
    expect(growing_strings(['fo', 'foo', 'oo'])).to eq(2)
  end

end
