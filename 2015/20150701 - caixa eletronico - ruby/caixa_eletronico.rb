def sacar(valor)
  notas = [10, 20, 50, 100]
  saque = []

  if valor >= 100
    saque << 100
    valor -= 100
  end
  if valor >= 100
    saque << 100
    valor -= 100
  end
  if valor >= 50
    saque << 50
    valor -= 50
  end
  if valor >= 50
    saque << 50
    valor -= 50
  end
  if valor >= 20
    saque << 20
    valor -= 20
  end
  if valor >= 20
    saque << 20
    valor -= 20
  end
  if valor >= 10
    saque << 10
    valor -= 10
  end

  saque.sort

end