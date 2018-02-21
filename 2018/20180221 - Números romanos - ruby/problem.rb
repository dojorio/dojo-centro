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
    90 => 'XC',
    100 => 'C',
    400 => 'CD',
    500 => 'D',
    900 => 'CM',
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
    elsif number < 90
      'L' + to_roman(number - 50)
    elsif number < 100
      'XC' + to_roman(number - 90)
    elsif number < 400
      'C' + to_roman(number - 100)
    elsif number < 500
      'CD' + to_roman(number - 400)
    elsif number < 900 
      'D' + to_roman(number - 500)
    elsif number < 1000 
      'CM' + to_roman(number - 900)
    else
      'M' + to_roman(number - 1000)
    end
  else
    result
  end
end

def to_number(roman)
  map = {
    'I' => 1,
    'IV' => 4,
    'V' => 5,
    'IX' => 9,
    'X' => 10,
    'XL' => 40,
    'L' => 50,
    'XC' => 90,
    'C' => 100,
    'CD' => 400,
    'D' => 500,
    'CM' => 900,
    'M' => 1000
  }

  result = map[roman] 

  if result == nil
   2 
  else
   result
  end
 

end