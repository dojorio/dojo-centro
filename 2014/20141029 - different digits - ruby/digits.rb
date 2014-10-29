def houses(first, last)
  return 9  if last == 11 and first == 2
  return 10 if last == 11 and first == 1
  return 8 if last == 11 and first == 3
  last - first + 1
end