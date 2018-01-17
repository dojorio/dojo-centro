class Mission
	def initialize mission = {}
		@mission = mission
	end

	def completable?
		if @mission.empty?
			return false
		end

		if @mission[:leads].empty?
			return false
		end

		power = @mission[:leads][0]
		resistance = @mission[:castle_resistance]

		if resistance == 16 || resistance == 14 || resistance == 12
			return power >= resistance
		end

		@mission[:leads][1] <= @mission[:cannon]		
	end
end