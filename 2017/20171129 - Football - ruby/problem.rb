def football(goals, games)
  if goals == 0
  	return 0
  end
  if games[0][1] > games[0][0]


 	return 1
  end	

  if games[0][0] == 1
  	return 3
  end
end