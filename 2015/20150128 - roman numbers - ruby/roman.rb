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

  if integer == 2 || integer == 3
    roman_number
  else
    roman_numbers[integer]
  end
end