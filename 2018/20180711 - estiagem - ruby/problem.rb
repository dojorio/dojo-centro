class Drying
  def initialize(houses)
    @houses = houses
  end 
  
  def averages_per_capta
    @houses.reduce(Hash.new(0)) do |result, house|
      result[house[1]/house[0]] += house[0]
      result
    end
  end

  def average_total
    pessoas, consumer = @houses.reduce([0, 0]) do |total, house|
      [total[0] + house[0], total[1] + house[1]]
    end

    consumer.fdiv(pessoas)
  end
end