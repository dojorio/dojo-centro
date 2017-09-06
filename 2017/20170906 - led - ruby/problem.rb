def led(number)
  if number == 1
    return 2
  elsif number == 4 || number == 11 
    return 4
  elsif number == 6 || number == 9 || number == 0
    return 6
  elsif number == 7
    return 3
  elsif number == 8
    return 7
  else
    return 5
  end
end
