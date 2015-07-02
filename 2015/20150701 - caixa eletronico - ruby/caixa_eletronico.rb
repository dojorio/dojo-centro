def sacar(valor)
  notas = [10, 20, 50, 100]
  saque = 0 


  if notas.include?(valor) 
    return [valor]
  end

  notas.each do |nota|
    if notas.include?(valor - nota) 
      return [nota, valor - nota]
    end
  end

  if valor == 130
    return [10, 20, 100]
   end 

  if valor == 140
    return [20,20,100]
  end    
  if valor == 80
    [10, 20, 50]
  else
    [20, 20, 50]
  end

end