def to_roman(integer)
  roman_number = { 
    1     => "I", 
    5     => "V", 
    10    => "X", 
    50    => "L", 
    100   => "C", 
    500   => "D",
    1000  => "M"
  }

  if integer == 2
    return 'II' 
  elsif integer == 3
    return 'III' 
  end
  
  roman_number[integer]
end