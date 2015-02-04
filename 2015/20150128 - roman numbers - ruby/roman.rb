def to_roman(integer)
  roman_numbers = { 
    1     => "I",
    5     => "V",
    10    => "X",
    50    => "L",
    100   => "C",
    500   => "D",
    1000  => "M"
  }

  latin_numbers = roman_numbers.keys.sort{|a,b| b <=> a}

  latin_numbers.each do ||

  # while integer > 0
  #   iterator = 7
  #   if roman_number.at[]
      
  #   end
  # end

  # if integer == 2 || integer == 3
  #   roman_number = roman_numbers[1] * integer
  # elsif integer == 20 || integer == 30
  #   roman_number = roman_numbers[10] * (integer / 10)
  # elsif integer == 200 || integer == 300
  #   roman_number = roman_numbers[100] * (integer / 100)
  # else
  #   roman_numbers[integer]
  # end

end