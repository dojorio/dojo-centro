def help_cupid(timezones)
  timezones.sort!

  last = timezones[-1] - timezones[-2]
  first = timezones[1] - timezones[0]

  middle = timezones[-2] - timezones[1]
  edge = timezones[-1] - timezones[0]

  if  24 - first < first
    first = 24 - first
  end

  if  24 - last < last
    last = 24 - last
  end

  if  24 - middle < middle
    middle = 24 - middle
  end

  if  24 - edge < edge
    edge = 24 - edge
  end

  [[last, first].max, [middle, edge].max].min
end