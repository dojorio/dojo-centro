def growing_strings(strings)
  return 0 if strings.empty?

  map_count = Hash.new([])

  strings.each do |string1|
    strings.reverse.each do |string2|
      if string1.include?(string2) && string1 != string2
        map_count[string1] += [string2]
      end
    end
  end

  nexxt = map_count.reduce([]) do |memo, (k,v)|
    memo.count < v.count ? v : memo
  end

  puts nexxt
  growing_strings(nexxt) + 1
end