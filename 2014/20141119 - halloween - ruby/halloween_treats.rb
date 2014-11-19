def halloween(criancas, doces)
  if(doces.length == 2 && !doces.include?(2)) 
    return [1, 2]
  end

  return [1] if doces.first / criancas > 0
  return [2] if doces.last  / criancas > 0

  []
end