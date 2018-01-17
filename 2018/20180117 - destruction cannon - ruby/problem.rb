class Mission
	def completable?

		if ! @mission.empty? && ! @mission[:leads].empty?
			@mission[:leads][1] <= @mission[:cannon]
		end
		
		if @mission[:castle_resistance] > @mission[:leads][0]
		return false
		end
	end

	def initialize mission = {}
		@mission = mission
	end
end