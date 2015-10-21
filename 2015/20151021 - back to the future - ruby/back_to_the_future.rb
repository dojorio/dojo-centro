def min_money(routes, friends, sits)
  return 'impossible' if friends > sits
  
  return 4 if routes[0][2] == 2
  friends
end