def bdc(size, grid)
  
  grid.transpose.map do |line|
    line.join.split('0').count do |palito|
      palito.size >= size
    end
  end.reduce(:+)
end