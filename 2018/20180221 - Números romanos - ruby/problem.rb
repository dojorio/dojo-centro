def to_roman(number)
  map = {
    1 => 'I',
    5 => 'V',
    10 => 'X',
    50 => 'L',
    100 => 'C',
    500 => 'D',
    1000 => 'M'
  }

  result = map[number]

  if result == nil
    case number
    when 2, 3
      'I' + to_roman(number - 1)
    when 6, 7, 8
      'V' + to_roman(number - 5)
    when 11, 12, 13
      'X' + to_roman(number - 10)
    end
  else  
    result
  end
end