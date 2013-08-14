def base(alien)
  result = 0
  characters = alien.split('')
  base = characters.uniq.length

  characters.reverse.each_with_index do |char, index|
    result += base**index if char == characters.first
  end

  return result
end
