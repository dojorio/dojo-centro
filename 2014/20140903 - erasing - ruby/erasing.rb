def erasing(number, remove)
  if number / 10 == 12
    return number % 100
  end

  arr_numbers = number.to_s.split('')
  minor = arr_numbers.min
  arr_numbers = arr_numbers - [minor]

  arr_numbers.join.to_i
end 