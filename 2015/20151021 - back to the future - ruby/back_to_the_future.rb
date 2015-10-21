def min_money(routes, friends, sits)
  return 'impossible' if friends > sits

  routes = routes.sort_by { |route| route[1] }

  if routes.last[0] == 2
    return friends * routes.map(&:last).reduce(0, :+)
  end

  friends * routes.last[2]
end