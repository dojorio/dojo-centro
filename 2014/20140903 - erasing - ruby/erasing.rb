def erasing(number, remove)
  arr_numbers = number.to_s.split('').sort.reverse

  return arr_numbers[1..remove]

  if number > 100
    return [number % 100, number / 10, number % 10 + (number / 100) * 10].max
  end

  if number.to_s[0] > number.to_s[1]
    return number.to_s[0].to_i
  end

  return number.to_s[1].to_i
end 