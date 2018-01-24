class WorldCup
  def initialize(matches, teams)
    @matches = matches
    @teams = teams
  end
  def draws 
    if @matches == 1 and @teams.values.include?(3)
      0
    end
    @matches
  end
end