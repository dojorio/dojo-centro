class Mission
	def completable?
		! @mission.empty? && ! @mission[:leads].empty?
	end 
	def initialize mission = {}
		@mission = mission
	end 
end