def base(alien)
  return 3 if alien.length == 2 and alien[0] == alien[1]
  alien.length
end
