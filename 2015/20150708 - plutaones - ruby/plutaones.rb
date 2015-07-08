class String
  def to_plu
    syllabus_textus = self.scan /.+?[aeiou]?/
    
    syllabus_textus.map do |st|
      "#{st}pl#{st[-1]}"
    end  
  end  
end