require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1023

describe "problem" do
  it "1 person, 10 used" do
    houses = [[1, 10]]
    drying = Drying.new(houses)

    expect(drying.averages_per_capta).to eq({ 10 => 1 })
  end

  it "2 person, 10 used" do
    houses = [[2, 10]]
    drying = Drying.new(houses)

    expect(drying.averages_per_capta).to eq({ 5 => 2 })
  end

  it "2 person, 8 used" do
    houses = [[2, 8]]
    drying = Drying.new(houses)

    expect(drying.averages_per_capta).to eq({ 4 => 2 })
  end

  it "2 houses: (2 person, 8 used), (1 person, 10 used)" do
    houses = [[2, 8], [1, 10]]
    drying = Drying.new(houses)

    expect(drying.averages_per_capta).to eq({ 4 => 2 , 10 => 1})
  end

  it "2 houses: (2 person, 8 used), (2 person, 10 used)" do
    houses = [[2, 8], [2, 10]]
    drying = Drying.new(houses)

    expect(drying.averages_per_capta).to eq({ 4 => 2 , 5 => 2})
  end

  it "2 houses: (2 person, 8 used), (2 person, 9 used)" do
    houses = [[2, 8], [2, 9]]
    drying = Drying.new(houses)

    expect(drying.averages_per_capta).to eq({ 4 => 4 })
  end

end
