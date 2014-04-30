
def mina(tabuleiro)
  if tabuleiro.join == '.....*' || tabuleiro.last == '*..' || tabuleiro.first == '..*'
    return 2
  end

  if tabuleiro.join.count('*') > 0
    tabuleiro.join.count('.')
  else
    1
  end
end

def conta_mina(tabuleiro, x, y)
  def a(x, y)
    tabuleiro[x][y] == '*' ? 1 : 0
  end
  a(x-1, y-1) +
  a(x-1, y) +
  a(x-1, y+1) +
  a(x, y-1) +
  a(x, y+1) +
  a(x+1, y-1) +
  a(x+1, y) +
  a(x+1, y+1)
end

def click!(tabuleiro, x, y)
  tabuleiro[x][y] = conta_mina(tabuleiro, x, y).to_s
end