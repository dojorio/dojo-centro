def nobody_solved_all(test)
    test.each do |contestant|
      return 0 if contestant.count(1) == contestant.length
    end

    1
end

def every_problem_solved(test)
  test = test.transpose

  test.each do |problem|
    return 0 if problem.count(0) == problem.length
  end

  1
end

def no_problem_solved_by_everyone(test)
  return 1 if (test[0][0] == 0 &&
              test[0][1] == 0 &&
              test[0][2] == 0) ||
              test[1][0] == 0
  0
end