def erasing(number, remove)
  if number > 100
    [number % 100, number / 10, number % 10 + (number / 100) * 10].max
  end

  if number.to_s[0] > number.to_s[1]
    return number.to_s[0].to_i
  end

  return number.to_s[1].to_i
end 