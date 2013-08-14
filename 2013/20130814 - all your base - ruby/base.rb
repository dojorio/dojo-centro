def base(alien)
  qtd_simbolos = alien.split('').uniq.length
  if qtd_simbolos == 2
    2
  else
    2**alien.length-1
  end
end
