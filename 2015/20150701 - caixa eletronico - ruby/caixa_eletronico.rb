def sacar(valor)

  notas = [10, 20, 50, 100]

  if notas.include?(valor) 
    return [valor]
  end

  if notas.include?(valor - 10) 
    return [10, valor - 10]
  end


  if notas.include?(valor - 20)
    return [20, valor - 20]
  end

  if valor == 150
    return [50, 100]
   end
   
   if valor == 200
     return [100, 100] 
   end  
end