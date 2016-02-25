def encrypt(str)
  str = str.split('')

  resp = ''

  str.reverse.each do |letter|
    resp += transform(letter)
  end
  resp[0] = (resp[0].ord + 1).chr if str.length > 1
  resp
end

def transform(letter)
  if ('a' <= letter && letter <= 'z') || ('A' <= letter && letter <= 'Z')
    return (letter.ord + 2).chr
  end

  (letter.ord - 1).chr
end