def testeValidaSession(session)
  session.flatten.uniq.count == 9
end
