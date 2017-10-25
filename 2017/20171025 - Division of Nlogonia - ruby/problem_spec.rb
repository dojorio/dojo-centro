require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1091

describe "Division of Nlogonia" do
  it "division (0, 0) points (0, 0)" do
    division = [0, 0]
    points   = [[0, 0]]
    expect(division_of_nlogonia(division, points)).to eq(['divisa'])
  end
end
