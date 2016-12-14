require_relative 'problem'

describe "game_of_life" do
  it "entra vazio" do
    grid = [[]]
    expect(game_of_life(grid)).to eq([[]])
  end

  it "entra valor 1 apenas" do
    grid = [[1]]
    expect(game_of_life(grid)).to eq([[0]])
  end

  it "entra valor 0 apenas" do
    grid = [[0]]
    expect(game_of_life(grid)).to eq([[0]])
  end

  it "entra 1, 1" do
    grid = [[1, 1]]
    expect(game_of_life(grid)).to eq([[0, 0]])
  end

  it "entra 1, 0" do
    grid = [[1, 0]]
    expect(game_of_life(grid)).to eq([[0, 0]])
  end


  it "entra 1, 1, 0" do
    grid = [[1, 1, 0]]
    expect(game_of_life(grid)).to eq([[0, 0, 0]])
  end


  it "entra 1, 1, 1" do
    grid = [[1, 1, 1]]
    expect(game_of_life(grid)).to eq([[0, 1, 0]])
  end

  it "entra 1, 1, 1 , 1" do
    grid = [[1, 1, 1, 1]]
    expect(game_of_life(grid)).to eq([[0, 1, 1, 0]])
  end

end
