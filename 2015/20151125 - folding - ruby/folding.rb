def fold_test(tape_in, tape_out)
  return false if tape_out.size > tape_in.size

  if tape_out.size == tape_in.size
    return true if tape_in == tape_out || tape_in.reverse == tape_out
    return false if tape_in[0] != tape_out[0] 
  end


  ##return true if tape_out == [3]

  false
end