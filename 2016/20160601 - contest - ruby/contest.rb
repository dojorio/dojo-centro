def nobody_solved_all(test)
    result = 0

    test.each do |contestant|
      result = 1 if contestant.count(1) < 3

    end
    return 

    # return 1 if test[0].count(1) < 3 &&
    #             test[1].count(1) < 3 &&
    #             test[2].count(1) < 3
    0

end