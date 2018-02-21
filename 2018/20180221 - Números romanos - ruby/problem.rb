def to_roman(number)
  map = {
    0 => '',
    1 => 'I',
    4 => 'IV',
    5 => 'V',
    9 => 'IX',
    10 => 'X',
    40 => 'XL',
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

    elsif number < 40
        'X' + to_roman(number - 10)

    elsif number < 50
        'XL' + to_roman(number - 40)
      
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