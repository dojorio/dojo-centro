def sacar(valor)
  notas = [100, 50, 20, 10]
  saque = []

  notas.each do |nota|
    while valor >= nota
      saque.unshift nota
      valor -= nota
    end
  end

  saque
end