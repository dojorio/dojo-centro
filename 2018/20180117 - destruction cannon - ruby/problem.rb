class Mission
	def completable?
		if @mission[:castle_resistance] == 16 # 10 < 16
			return false
		end

		if @mission[:castle_resistance] == 14 # 10 < 14
			return false
		end
		
		if @mission[:castle_resistance] == 12 # 10 < 12
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