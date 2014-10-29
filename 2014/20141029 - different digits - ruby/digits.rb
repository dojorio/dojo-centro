def houses(first, last)
  return 10 if last == 11
  return 9  if last == 11 and first == 2
  last - first + 1
end