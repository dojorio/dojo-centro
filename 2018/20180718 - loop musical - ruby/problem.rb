def musical_loop(magnitudes)
  if magnitudes.length > 3
    if (magnitudes[0] <=> magnitudes[1]) == (magnitudes[1] <=> magnitudes[2])
      return 2
    else
      return 4
    end
  end

  2
end