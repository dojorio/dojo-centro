def help_cupid(timezones)
  if timezones.first != timezones.last
    return 1
  end

  0
end