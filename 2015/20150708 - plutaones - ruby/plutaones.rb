class String
  def to_plu
    syllabus_textus = self.scan /[^aeiou]*([aeiou]|$)/

    syllabus_textus.map do |st|
      "#{st}pl#{st[-1]}"
    end.join
  end  
end