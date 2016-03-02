def encrypt(str)
  str = str.split('')

  resp = ''

  str.reverse.each do |letter|
    resp += transform(letter)
  end
  (str.length/2).times do |i|
    resp[i] = (resp[i].ord + 1).chr 
  end
  resp
end

def transform(letter)
  if ('a' <= letter && letter <= 'z') || ('A' <= letter && letter <= 'Z')
    return (letter.ord + 2).chr
  end

  (letter.ord - 1).chr
end