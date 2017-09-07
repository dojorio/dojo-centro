def led(number)
  results = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

  number.to_s.split("").map(&:to_i).reduce(0) do |leds, number|
    leds + results[number]
  end
end