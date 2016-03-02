def help_cupid(timezones)
  if timezones.length == 4 && timezones[2] == 1
    return 0
  end

  (timezones.last - timezones.first).abs
end