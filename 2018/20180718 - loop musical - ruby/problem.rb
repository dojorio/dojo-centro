def musical_loop(magnitudes)
  count = 0
  magnitudes.each_with_index do |num, i|
    ind1 = (i+1) % magnitudes.length
    ind2 = (i+2) % magnitudes.length
    if (num <=> magnitudes[ind1]) != (magnitudes[ind1] <=> magnitudes[ind2])
      count += 1    
    end
  end
  return count
end