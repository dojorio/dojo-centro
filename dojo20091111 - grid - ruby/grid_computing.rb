class Grid
  def initialize(grid)
    @grid = grid
  end
  
  def sum
    matrix = []
    begin 
      arr = @grid.split("\n")
      matrix << arr[0].split(" ")
      matrix << arr[1].split(" ")
    rescue
      return @grid.to_i
    end
  
    lines_sum = [0, 0]
    colums_sum = [0, 0]
    
    max = 0
    
    matrix.each do  |linha|
           linha.collect! do |coluna| 
        coluna.to_i
      end
    end
     
    matrix.each do  |linha|
      sum_linha = linha[0]  + linha[1]
      max = sum_linha if  max < sum_linha
    end  
    max
  end
    
end

#12
#34