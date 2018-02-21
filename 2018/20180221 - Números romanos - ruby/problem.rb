def to_roman(number)
  map = {
    0 => '',
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
      if number == 4
        'IV'
      else
        'I' + to_roman(number - 1)
      end
    elsif number < 10
      if number == 9
        'IX'
      else
        'V' + to_roman(number - 5)
      end
    elsif number < 50
      if number >= 40
        'XL' + to_roman(number - 40)
      else
        'X' + to_roman(number - 10)
      end
    elsif number < 100
      'L' + to_roman(number - 50)
    elsif number < 500
      'C' + to_roman(number - 100)
    elsif number < 1000 
      'D' + to_roman(number - 500)
    else
      'M' + to_roman(number - 1000)
    end
  else
    result
  end
end