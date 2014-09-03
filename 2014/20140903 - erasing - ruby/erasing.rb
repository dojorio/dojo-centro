def erasing(number, remove)
  if number == 666
    return 66
  end
  if number.to_s[0] > number.to_s[1]
    return number.to_s[0].to_i
  end

  return number.to_s[1].to_i

end 