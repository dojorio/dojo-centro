def encrypt(str)
  str = str.split('')
  resp = ''
  str.each do |letter|
    resp += transform(letter)
  end
  return resp
  return 'dc' if str == 'aa'

  transform(str)
end

def transform(letter)
  if ('a' <= letter && letter <= 'z') or ('A' <= letter && letter <= 'Z')
    return (letter.ord + 2).chr
  end

  (letter.ord - 1).chr
end