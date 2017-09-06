def led(number)
  numbers = number.to_s.split ""
  leds = 0

  numbers.each do |number|
    number = number.to_i

    if number == 1
      leds += 2
    elsif number == 4
      leds += 4
    elsif number == 6 || number == 9 || number == 0
      leds += 6
    elsif number == 7
      leds += 3
    elsif number == 8
      leds += 7
    else
      leds += 5
    end
  end
  
  leds
end