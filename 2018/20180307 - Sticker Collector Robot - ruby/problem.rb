def execution(arena, instructions)
  if instructions == ''
  	return 0
  end

  if arena[0].include?('*') and instructions.include?('F')
  	return 1
  end

  if arena == ['L']
  	return 0
  end
  0
end