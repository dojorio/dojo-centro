def growing_strings(strings)
  map_count = Hash.new(0)

  strings.each do |string1|
    strings.reverse.each do |string2|
      if string1.include?(string2) && string1 != string2
        map_count[string1] += 1
      end
    end
  end

  map_count
end