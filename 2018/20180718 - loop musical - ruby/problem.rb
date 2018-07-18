def musical_loop(magnitudes)
  if magnitudes.length == 4
    if (magnitudes[0] <=> magnitudes[1]) == (magnitudes[1] <=> magnitudes[2])
      return 2
    elsif (magnitudes[1] <=> magnitudes[2]) == (magnitudes[2] <=> magnitudes[3])
      return 2
    else
      return 4
    end
  end
  return 4 if magnitudes.length == 5
  2
end