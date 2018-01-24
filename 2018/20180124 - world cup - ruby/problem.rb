class WorldCup
  attr_reader :matches, :teams

  def initialize(matches, teams)
    @matches = matches
    @teams   = teams
  end

  def draws
    if matches == teams.values.first
      matches
    else
      teams.values.first % 3
    end
  end
end