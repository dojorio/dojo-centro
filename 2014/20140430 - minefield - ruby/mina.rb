
def mina(tabuleiro)
  total = 0
  (0...tabuleiro.size).each do |i|
    (0...tabuleiro[i].size).each do |j|
      if tabuleiro[i][j] == '.' && conta_mina(tabuleiro, i, j) == 0
        click!(tabuleiro, i, j)
        total += 1
      end
    end
  end
  (0...tabuleiro.size).each do |i|
    (0...tabuleiro[i].size).each do |j|
      if tabuleiro[i][j] == '.'
        click!(tabuleiro, i, j)
        total += 1
      end
    end
  end

  total
end

def conta_mina(t, x, y)
  def a(t, x, y)
    return 0 if x<0 || y<0
    t[x][y].count('*')
  rescue
    0
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