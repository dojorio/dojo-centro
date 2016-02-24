def encrypt(str)
  arr = str.split('')
  return (str.ord + 2).chr if str.ord > 96 && str.ord < 123
  return (str.ord + 2).chr if str.ord > 64 && str.ord < 91
  (str.ord - 1).chr
end