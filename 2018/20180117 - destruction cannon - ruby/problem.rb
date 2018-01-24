class Mission
	def initialize mission = {}
		@mission = mission
 	
		@resistance = @mission[:castle_resistance]
		@capacity = @mission[:cannon]
        @leads = Array(mission[:leads])
        @weight = @leads[1]
		@power = @leads[0]
 	end

	def completable?
		return false if @mission.empty? || @leads.empty?
		@power >= @resistance && @weight <= @capacity
	end
end