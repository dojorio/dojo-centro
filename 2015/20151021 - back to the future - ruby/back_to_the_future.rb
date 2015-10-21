def min_money(routes, friends, sits)

  return 'impossible' if friends > sits

  routes = routes.sort_by { |route| route[1] }
  
  return friends * 2 if routes.last[0] == 2

  friends * routes.last[2]
end