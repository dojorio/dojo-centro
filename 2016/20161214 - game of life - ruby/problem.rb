def game_of_life(grid)
  line = grid[0]

  result = Array.new(line.size, 0)

  if line.reduce(:+) == line.size
    1.upto(line.size-2) do |n|
      result[n] = 1
    end
  end

  [ result ]
end
