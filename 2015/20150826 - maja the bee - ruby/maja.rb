def maja_coord(willi)
  x = 0, y = 0

  x = case willi
      when 1, 2, 5
        0
      when 3, 4
        -1
      when 6, 7, 8
        1
      end

  y = case willi
      when 1, 4, 7
        0
      when 5, 6
        -1
      when 2, 3, 8
        1
      end

  [x, y]
end