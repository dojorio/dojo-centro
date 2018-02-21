def to_roman(number)
  case number
   when 1
  	'I'
  when 5
  	'V'
  when 10
  	'X'
  when 50 
  	'L'
  when 100
    'C'
  else
  	'D'
  end
end