def to_roman(number)
  case number
  when 1
    'I'
  when 2, 3
    'I' + to_roman(number - 1)
  when 5
    'V'
  when 6, 7
    'V' + to_roman(number - 5)
  when 10
    'X'
  when 50 
    'L'
  when 100
    'C'
  when 500
    'D'
  else
    'M'
  end
end