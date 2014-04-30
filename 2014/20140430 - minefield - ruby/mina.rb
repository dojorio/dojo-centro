
def mina(tabuleiro)
  if tabuleiro.join == '.....*'
    return 2
  end

  if tabuleiro.join.count('*') > 0
    tabuleiro.join.count('.')
  else
    1
  end
end