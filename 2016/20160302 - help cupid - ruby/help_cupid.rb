def help_cupid(timezones)
  timezones.sort!

  last = (timezones[-1] - timezones[-2]).abs
  first = (timezones[1] - timezones[0]).abs

  middle = (timezones[-2] - timezones[1]).abs
  edge = (timezones[-1] - timezones[0]).abs

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

  [last + first, middle + edge].min/2
end