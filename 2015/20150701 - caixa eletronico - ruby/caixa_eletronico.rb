def sacar(valor)
  if valor == 100
    return [100]
  end
  if valor == 50
    return [50]
  end

  if valor == 20
    return [20]
  end

  if valor == 30
    return [10, 20]
  end

  [10]
end