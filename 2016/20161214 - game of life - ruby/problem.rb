def game_of_life(grid)
  line = grid[0]


  line.each_with_index.map do |n, i|
    prev = i == 0 ? 0 : line[i - 1] 
    nex = line[i + 1] || 0
    if prev == 1 && nex == 1 
      n 
    else 
      0
    end
  end
 
end
