def execution(arena, instructions)
  if (instructions == '' or 
  	!instructions.include?('F') or 
  	!arena[0].include?('*') or 
  	arena[0].include?('N') or 
  	arena[0].include?('S') )
  		return 0
  end



  if arena[0].include?('*') and ( instructions.include?('F') and !instructions.include?('D') )
  		return 1
  end

  return 0
end