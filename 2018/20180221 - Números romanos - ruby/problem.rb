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
    if number < 5
      'I' + to_roman(number - 1)
    elsif number < 10
      'V' + to_roman(number - 5)
    elsif number < 50
      'X' + to_roman(number - 10)
    else
      'L' + to_roman(number - 50)
    end
  else
    result
  end
end