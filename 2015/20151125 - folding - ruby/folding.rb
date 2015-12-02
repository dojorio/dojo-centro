def fold_test(tape_in, tape_out)
  return false if tape_out.size > tape_in.size

  if tape_out.size == tape_in.size
    return tape_in == tape_out || tape_in.reverse == tape_out
  end

  if tape_out.size == 1
    return true if tape_in.reduce(:+) == tape_out.first
  else 
    return tape_in.reduce(:+) == tape_out.reduce(:+)
  end

if tape_out.size == 2
    return tape_in.reduce(:+) == tape_out.reduce(:+)
  end
end
