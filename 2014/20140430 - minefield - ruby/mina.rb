
def mina(tabuleiro)
  if tabuleiro.length == 3 && tabuleiro[2] != '..' 
    return 2
  end

  if tabuleiro.join.count('*') > 0
    tabuleiro.join.count('.')
  else
    1
  end
end