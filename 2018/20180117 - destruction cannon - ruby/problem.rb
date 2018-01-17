class Mission
	def completable?
		if @mission[:castle_resistance] == 12
		return false
		end

		if ! @mission.empty? && ! @mission[:leads].empty?
			@mission[:leads][1] <= @mission[:cannon]
		end
	end

	def initialize mission = {}
		@mission = mission
	end
end