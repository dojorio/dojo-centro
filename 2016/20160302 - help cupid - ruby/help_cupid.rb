def help_cupid(timezones)
  timezones.sort!

  last = timezones[-1] - timezones[-2]
  first = timezones[1] - timezones[0]

  [last, first].max
end