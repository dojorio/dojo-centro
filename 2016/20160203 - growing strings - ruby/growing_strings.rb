def growing_strings(strings)
  if strings.length == 3
    if strings[1].include?(strings[0])
      return 3
    else
      return 2
    end
  end

  if strings.count == 2
    return 2 if strings[1].include?(strings[0]) || strings[0].include?(strings[1])
  end
  1
end