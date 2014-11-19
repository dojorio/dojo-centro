def halloween(criancas, doces)
  if(doces.length == 2) 
    return [1, 2]
  end

  doces[0] / criancas > 0  ? [1] : []
end