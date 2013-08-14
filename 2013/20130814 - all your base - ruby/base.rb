def base(alien)
  result = 0
  leftmost = alien[0]
  alien.split('').reverse.each_with_index do |c, i|
    if c == leftmost
      result += 2**i
    end
  end
  return result

  unique_simbolos = alien.split('').uniq

  if alien == 'aac'
    6
  elsif unique_simbolos.length == 2
    2 ** (alien.length-1)
  else
    2 **alien.length-1
  end
end
