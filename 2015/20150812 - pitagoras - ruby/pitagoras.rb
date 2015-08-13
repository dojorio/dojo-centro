def pitagoras(*lista)
  result = 'tripla'
  lista.sort!

  if lista[0] ** 2 + lista[1] ** 2 == lista[2] ** 2
    result << ' pitagorica'

    if lista[2].gcd(lista[1].gcd(lista[0])) == 1
      result << ' primitiva'
    end

  end

  result
end