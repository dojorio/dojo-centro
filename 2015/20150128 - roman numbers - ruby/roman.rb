def to_roman(integer)
  if (integer == 1)
    'I'
  elsif (integer == 5)
    'V'
  elsif (integer == 10)  
    'X'
  elsif (integer == 50)  
    'L'
  elsif (integer == 100)
    'C'
  elsif (integer == 500)
    'D'
  else
    'M'
  end
end