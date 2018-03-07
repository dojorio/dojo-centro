def execution(arena, instructions)
  if instructions == '' or !arena[0].include?('*') or instructions== 'N'
  		return 0
  end

  if arena[0].include?('*') and instructions.include?('F')
  		return 1
  end
end