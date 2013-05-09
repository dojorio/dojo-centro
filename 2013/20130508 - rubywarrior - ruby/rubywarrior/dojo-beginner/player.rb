class Player
  def play_turn(warrior)
    @last_health ||= warrior.health

    scavenger(warrior)

    @last_health = warrior.health
  end

  def scavenger(warrior)
    ahead = warrior.look
    has_captive_ahead = ahead.detect { |s| s.captive? }
    has_something_ahead = ahead.detect { |s| !s.empty? && !s.wall? }

    if warrior.feel.captive?
      warrior.rescue!
    elsif !has_something_ahead || has_captive_ahead
      act!(warrior)
    else
      warrior.shoot!
    end
  end

  def act!(warrior)
    taking_damage = warrior.health < @last_health
    recover = !taking_damage && warrior.health < 20
    fallback = taking_damage && warrior.health < 8

    if fallback
      warrior.walk! :backward
    elsif recover
      warrior.rest!
    else
      warrior.walk!
    end
  end

end

class WarriorWalk
  def initialize(warrior)
    @warrior = warrior
  end

end
