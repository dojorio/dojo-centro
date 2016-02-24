def encrypt(str)
  return (str.ord + 2).chr if str.ord > 96
  return (str.ord + 2).chr if str.ord > 64
  return (str.ord - 1).chr if str != 'a'

end