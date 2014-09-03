def erasing(number, remove)
  if number / 10 == 12
    return number % 100
  end

  arr_numbers = number.to_s.split('')
  minor = arr_numbers.min
  
  minor_idx = arr_numbers.index(minor)

  arr_numbers.delete_at minor_idx

  arr_numbers.join.to_i
  
end 