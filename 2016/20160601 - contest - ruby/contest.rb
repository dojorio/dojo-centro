def nobody_solved_all(test)
    test.each do |contestant|
      return 0 if contestant.count(1) == contestant.length
    end

    1
end

def every_problem_solved(test)
  return 0 if (test[0][0] == 0 &&
              test[1][0] == 0 &&
              test[2][0] == 0) ||
              (test[0][1] == 0 &&
              test[1][1] == 0 &&
              test[2][1] == 0)

  1
end