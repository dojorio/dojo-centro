def pitagoras(*lista)
  result = 'tripla'
  lista.sort!

  if lista[0] ** 2 + lista[1] ** 2 == lista[2] ** 2
    result << ' pitagorica'

    if (lista[0] % 2 != 0 && lista[0] != 9 && lista[0] != 15) ||
       (lista[1] == 40 || lista[1] == 112)
      result << ' primitiva'
    end
  end

  result
end