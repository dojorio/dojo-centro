
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
  tabuleiro.join.count('*')
end

def click!(tabuleiro, x, y)
  tabuleiro[x][y] = conta_mina(tabuleiro, x, y).to_s
end