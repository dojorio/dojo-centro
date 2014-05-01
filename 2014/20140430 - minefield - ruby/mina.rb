
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

def conta_mina(t, x, y)
  def a(t, x, y)
    return 0 if x<0 || y<0
    t[x][y].count('*')
  end

  a(t, x-1, y-1) +
  a(t, x-1, y) +
  a(t, x-1, y+1) +
  a(t, x, y-1) +
  a(t, x, y+1) +
  a(t, x+1, y-1) +
  a(t, x+1, y) +
  a(t, x+1, y+1)
end

def click!(tabuleiro, x, y)
  if tabuleiro[x] && tabuleiro[x][y] == '.' && x>=0 && y>=0
    tabuleiro[x][y] = conta_mina(tabuleiro, x, y).to_s
    if tabuleiro[x][y] == '0'
      click!(tabuleiro, x-1, y-1)
      click!(tabuleiro, x-1, y)
      click!(tabuleiro, x-1, y+1)
      click!(tabuleiro, x, y-1)
      click!(tabuleiro, x, y+1)
      click!(tabuleiro, x+1, y-1)
      click!(tabuleiro, x+1, y)
      click!(tabuleiro, x+1, y+1)
    end
  end
end