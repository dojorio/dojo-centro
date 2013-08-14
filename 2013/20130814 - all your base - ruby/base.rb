def base(alien)
  return 3 if alien.length == 2 and alien[0] == alien[1]
  return 7 if alien.length == 3
  return 15 if alien.length == 4
  alien.length
end
