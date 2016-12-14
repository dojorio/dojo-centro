def game_of_life(grid)
  grid.map do |line|
    [
      line.each_index.map do |i|
        prev = i == 0 ? 0 : line[i - 1] 
        nex = line[i + 1] || 0

        prev + nex == 2 ? line[i] : 0
      end
    ]
  end
end
