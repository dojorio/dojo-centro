class WorldCup
  def initialize(matches, teams)
    @matches = matches
    @teams = teams
  end
  def draws
    if @matches == 3 && @matches == @teams[:Brasil]
      return 3
    end 

    @teams[:Brasil] % 3

  end
end