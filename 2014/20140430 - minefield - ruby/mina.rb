
def mina(tabuleiro)
  if tabuleiro.join.count('*') > 0
    tabuleiro.join.count('.')
  else
    1
  end
end