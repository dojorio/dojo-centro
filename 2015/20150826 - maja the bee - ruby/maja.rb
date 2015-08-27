def maja_coord(willi)
  if willi == 2
    return [0, 1]
  
  elsif willi == 3
    return [-1, 1]
  
  elsif willi == 4
    return [-1, 0]

  elsif willi == 5
    return [0, -1]
 

  elsif willi == 6
    return [1, -1]

  elsif willi == 7
    return [1, 0]

  elsif willi == 8
    return [1, 1]

  end

  [0, 0]
end