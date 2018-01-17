class Mission
	def completable?
		! @mission.empty?
	end 
	def initialize mission = {}
		@mission = mission
	end 
end