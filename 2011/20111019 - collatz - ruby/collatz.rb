def collatz(i, j)
  (i..j).map{|n| collatz_list(n)}.inject{|a,b|
    if b.length > a.length
      b
    else
      a
    end
  }[0]
end

def collatz_next(n)
  raise if n == 1 
  if (n % 2) == 0
    n/2
  else
    3 * n + 1
  end
end

def collatz_list(n)
  list = [n]
  while n > 1
    n = collatz_next(n)
    list << n 
  end
  list
end