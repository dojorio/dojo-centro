class String
  def to_plu
    scan(/[^aeiou]*./).map do |chunk|
      "#{chunk}pl#{chunk[-1]}"
    end.join
  end  
end