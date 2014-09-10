def erasing(number, remove)

  arr_numbers = number.to_s.split('')

  if arr_numbers.count < remove 
    return nil
  end

  minor = arr_numbers.min

  arr_numbers.delete_at(arr_numbers.index(minor))

  result = arr_numbers.join.to_i

  remove == 1 ? result : erasing(result, remove - 1)
end
