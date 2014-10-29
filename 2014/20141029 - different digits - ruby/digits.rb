def houses(first, last)
  return last - first - (last/ 11) + 1 # +1 = ceil
end