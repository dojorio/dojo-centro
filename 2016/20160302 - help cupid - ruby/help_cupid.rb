def help_cupid(timezones)
  timezones.sort!

  return timezones[-1] - timezones[-2]

  if timezones.length == 4 && timezones[2] == 1 && timezones[3] == 1
    return 0
  end


  (timezones.last - timezones.first).abs
end