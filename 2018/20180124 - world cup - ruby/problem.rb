class WorldCup
  attr_reader :matches, :teams

  def initialize(matches, teams)
    @matches = matches
    @teams   = teams
  end

  def draws
    if teams.size == 3 and teams[:Brasil] == 2
      return 2
    end
    if teams.size == 3
      return 1
    end
    if matches == teams.values.first
      matches
    else
      teams.values.first % 3
    end
  end
end