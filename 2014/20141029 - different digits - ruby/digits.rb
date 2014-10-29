def houses(first, last)
  (first..last).select do |num|
    str = num.to_s.split('')
    str.uniq.count == str.count
  end.count
end