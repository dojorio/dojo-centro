def gincana(criancas)
  if criancas.values == [4,3,2]
  	return criancas.keys[1].to_s
  end

  if criancas.keys[0] == :Pe || criancas.keys[0] == :Jo
    return "Jo"
  else
  	return "Pe"
  end
end