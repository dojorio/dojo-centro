def nobody_solved_all(test)

    test.each do |contestant|
      return 0 if contestant.count(1) == contestant.length

    end

    1

end