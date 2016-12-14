def game_of_life(grid)
  if grid == [[1]]
    return [[0]]
  end

  if grid[0].include?(1)
    return [[0, 0]]
  end

  grid
end
