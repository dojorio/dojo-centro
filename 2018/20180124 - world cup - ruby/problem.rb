class WorldCup
  attr_reader :matches, :teams

  def initialize(matches, teams)
    @matches = matches
    @teams   = teams
  end

  def draws
    if matches == teams[:Brasil]
      matches
    else
      teams[:Brasil] % 3
    end
  end
end