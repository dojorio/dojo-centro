require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1091

describe "Division of Nlogonia" do
  it "division (0, 0) points (0, 0)" do
    division = [0, 0]
    points   = [[0, 0]]
    expect(division_of_nlogonia(division, points)).to eq(['divisa'])
  end

  it "division (0, 0) points (1, 1)" do
    division = [0, 0]
    points   = [[1, 1]]
    expect(division_of_nlogonia(division, points)).to eq(['NE'])
  end

  it "division (0, 0) points (1, -1)" do
    division = [0, 0]
    points   = [[1, -1]]
    expect(division_of_nlogonia(division, points)).to eq(['SE'])
  end

  it "division (0, 0) points (-1, -1)" do
    division = [0, 0]
    points   = [[-1, -1]]
    expect(division_of_nlogonia(division, points)).to eq(['SO'])
  end

  it "division (0, 0) points (-1, 1)" do
    division = [0, 0]
    points   = [[-1, 1]]
    expect(division_of_nlogonia(division, points)).to eq(['NO'])
  end

  it "division (0, 0) points (0, 0), (0, 1)" do
    division = [0, 0]
    points   = [[0, 0], [0, 1]]
    expect(division_of_nlogonia(division, points)).to eq(['divisa', 'divisa'])
  end

  it "division (0, 0) points (0, 0), (1, 1)" do
    division = [0, 0]
    points   = [[0, 0], [1, 1]]
    expect(division_of_nlogonia(division, points)).to eq(['divisa', 'NE'])
  end

  it "division (0, 0) points (0, 0), (1, -1)" do
    division = [0, 0]
    points   = [[0, 0], [1, -1]]
    expect(division_of_nlogonia(division, points)).to eq(['divisa', 'SE'])
  end

  it "division (0, 0) points (0, 1), (1, 0) (0, 0)" do
    division = [0, 0]
    points   = [[0, 1], [1, 0], [0,0]]
    expect(division_of_nlogonia(division, points)).to eq(['divisa', 'divisa', 'divisa'])
  end

  it "division (1, 1) points(0, 0)" do
    division = [1, 1]
    points   = [[0, 0]]
    expect(division_of_nlogonia(division, points)).to eq(['SO'])
  end

  it "division (1, 1) points(0, 2)" do
    division = [1, 1]
    points   = [[0, 2]]
    expect(division_of_nlogonia(division, points)).to eq(['NO'])
  end

  it "division (1, 1) points(2, 0)" do
    division = [1, 1]
    points   = [[2, 0]]
    expect(division_of_nlogonia(division, points)).to eq(['SE'])
  end

  it "division (-1, -1) points(0, 0)" do
    division = [-1, -1]
    points   = [[0, 0]]
    expect(division_of_nlogonia(division, points)).to eq(['NE'])
  end
end
