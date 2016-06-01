def nobody_solved_all(test)
    test.each do |contestant|
      return 0 if contestant.count(1) == contestant.length
    end

    1
end

def every_problem_solved(test)
  test = test.transpose

  test.each do |problem|
    return 0 if problem.count(0) == 3
  end

  1
end