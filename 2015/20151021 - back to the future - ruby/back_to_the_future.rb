def min_money(routes, friends, sits)

  return 'impossible' if friends > sits

  friends * routes[0][2]
end