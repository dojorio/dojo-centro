def mictorios lista
  lista = '0' + lista + '0'
  mictorios_livre = 0

  1.upto (lista.size - 1) do |i|
    if lista[i] == '0' && lista[i+1] == '0' && lista[i-1] == '0'
      mictorios_livre += 1
    end
  end

  mictorios_livre
end