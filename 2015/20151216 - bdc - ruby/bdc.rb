def bdc(size, grid)
  return 0 if size > grid.size
  
  qtd = grid.transpose.map do |line|
    line.join.split('0').count do |palito|
      palito.size >= size
    end
  end

  qtd.reduce(:+)
end