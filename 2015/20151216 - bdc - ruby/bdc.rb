def bdc(size, grid)
  return 0 if size > grid.size
  
  count = 0
  
  grid.each do |line|
    line.each do |cell|
      if cell == 1
        count = cell == 0 ? count + 1 
      end
    end
  end

  count
end