require './casket_of_stars.rb'

describe "A casket of stars" do
  it "to stars 1, 2, 3 gets 3 sp" do
    expect(casket_of_stars([1, 2, 3])).to eq 3
  end

  it "to stars 1, 3, 2 gets 2 sp" do
    expect(casket_of_stars([1, 3, 2])).to eq 2
  end

  it "to stars 3, 2, 1 gets 3 sp" do
    expect(casket_of_stars([3, 2, 1])).to eq 3
  end

  it "to stars 3, 1, 2 gets 6 sp" do
    expect(casket_of_stars([3, 1, 2])).to eq 6
  end

  it "to stars 1, 1, 1, 1 gets 2 sp" do
    expect(casket_of_stars([1, 1, 1, 1])).to eq 2
  end

  it "to stars 1, 2, 1, 1 gets 3 sp" do
    expect(casket_of_stars([1, 2, 1, 1])).to eq 3
  end

  it "to stars 1, 1, 2, 1 gets 3 sp" do
    expect(casket_of_stars([1, 1, 2, 1])).to eq 3
  end

  it "to stars 2, 1, 2, 1 gets 6 sp" do
    expect(casket_of_stars([2, 1, 2, 1])).to eq 6
  end

  it "to stars 1, 2, 1, 2 gets 3 sp" do
    expect(casket_of_stars([1, 2, 1, 2])).to eq 6
  end

  it "to stars 2, 1, 1, 2 gets 6 sp" do
    expect(casket_of_stars([2, 1, 1, 2])).to eq 6
  end

  it "to stars 2, 1, 2, 20_000 gets 60_000 sp" do
    expect(casket_of_stars([2, 1, 2, 20_000])).to eq 60_000
  end

  it "to stars 1, 2, 3, 4 gets 12 sp" do
    expect(casket_of_stars([1, 2, 3, 4])).to eq 12
  end

  it "to stars 1, 1, 1, 1, 1 gets 3 sp" do
    expect(casket_of_stars([1, 1, 1, 1, 1 ])).to eq 3
  end

  it "to stars 2, 1, 1, 1, 1 gets 6 sp" do
    expect(casket_of_stars([2, 1, 1, 1, 1 ])).to eq 6
  end
end