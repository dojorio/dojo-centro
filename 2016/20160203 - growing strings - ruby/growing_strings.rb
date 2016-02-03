def growing_strings(strings)
  count = 0

  strings.each do |string1|
    strings.reverse.each do |string2|
      if string1.include?(string2)
        count += 1
      end
    end
  end

  count
end