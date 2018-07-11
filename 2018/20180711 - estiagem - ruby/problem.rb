class Drying
	def initialize(houses)
		@houses = houses
	end	
	def averages_per_capta()
		return { @houses[0][1]/@houses[0][0] => @houses[0][0] }
	end	
end