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
  map_1 = {
    'I' => 1,
    'V' => 5,
    'X' => 10,
    'L' => 50,
    'C' => 100,
    'D' => 500,
    'M' => 1000
  }

  map_2 = {
    'CM' => 900,
    'CD' => 400,
    'XC' => 90,
    'XL' => 40,
    'IX' => 9,
    'IV' => 4
  }

  result = map_1[roman] 

  if result == nil
    result = map_2[roman]
  end

  if result == nil
    keys  = map_2.keys
    total = 0

    keys.each do |key|
      if roman.include?(key)
        total = total + map_2[key]
        roman = roman.gsub(key, '')
      end
    end

    if roman.length > 0
      total + to_number(roman)
    else
      
  else
    result
  end
 

end