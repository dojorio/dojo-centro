class WorldCup
  def initialize(matches, teams)
    @matches = matches
    @teams = teams
  end
  def draws 
    if @teams.values.include?(2)
      return 2
    end
    if @teams.values.include?(3)
      return 0
    end
    @matches > 0 ? 1 : 0
  end
end