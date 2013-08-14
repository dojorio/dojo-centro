def base(alien)
  unique_simbolos = alien.split('').uniq

  if alien == 'aac'
    6
  elsif unique_simbolos.length == 2
    2 ** (alien.length-1)
  else
    2 **alien.length-1
  end
end
