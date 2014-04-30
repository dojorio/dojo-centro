
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

def tem_mina(tabuleiro, x, y)
  
end

def click!(tabuleiro, x, y)
  tabuleiro[x][y] = tabuleiro.join.count('*').to_s
end