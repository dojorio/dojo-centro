require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1023

describe "problem" do
  it "1 person, 10 used" do
    houses = [[1, 10]]
    drying = Drying.new(houses)

    expect(drying.averages_per_capta).to eq({ 10 => 1 })
    
  end
end
