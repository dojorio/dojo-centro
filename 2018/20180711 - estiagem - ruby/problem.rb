class Drying
  def initialize(houses)
    @houses = houses
  end 
  
  def averages_per_capta
    result = Hash.new(0)

    @houses.each do |house|
        result[house[1]/house[0]] += house[0]
    end    

    return result
  end 
end