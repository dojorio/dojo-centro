def min_money(routes, friends, sits)

  return 'impossible' if friends > sits

  routes = routes.sort_by { |route| route[1] }
  if routes.size == 1
    friends * routes[0][2]
  else
    friends * routes[1][2]
  end
end