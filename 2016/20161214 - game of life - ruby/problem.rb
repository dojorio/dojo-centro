def game_of_life(grid)
  grid.each_with_index.map do |line, idx_line|
    line.each_index.map do |i|
      prev = i == 0 ? 0 : line[i - 1] 
      nex = line[i + 1] || 0

      down = (grid[idx_line + 1]||[])[i] || 0
      up = (grid[idx_line -1]||[])[i] || 0

      neigh = prev + nex + down + up

      neigh == 2 || neigh == 3 ? line[i] : 0
    end
  end
end
