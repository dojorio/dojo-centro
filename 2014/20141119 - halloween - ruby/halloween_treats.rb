def halloween(criancas, doces)
  if(criancas == 1)
    return (1..doces.length).to_a
  end

  if(!doces.include?(2)) 
    return [1, 2]
  end


  return [1] if doces.first / criancas > 0
  return [2] if doces.last  / criancas > 0


  []
end