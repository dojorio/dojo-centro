def casket_of_stars(stars)
  if stars.count == 4
    sp_2_then_3 = stars.first * (stars[2] + stars.last)
    sp_3_then_2 = stars.last * (stars[1] + stars.first)

    return [sp_2_then_3, sp_3_then_2].max
  end

  if stars.count == 5
    return stars[1..-2].reduce(:+) * stars[0]
  end

  stars.first * stars.last
end