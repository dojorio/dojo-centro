def help_cupid(timezones)
  timezones.sort!

  last = timezones[-1] - timezones[-2]
  first = timezones[1] - timezones[0]

  if  24 - first < first
    first = 24 - first
  end

  [last, first].max
end