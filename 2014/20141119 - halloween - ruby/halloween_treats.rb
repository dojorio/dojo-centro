# https://www.urionlinejudge.com.br/judge/en/problems/view/1656
def halloween(criancas, doces)
  casas = (1..doces.length).to_a
  total_doces = doces.reduce(:+)

  return casas if total_doces % criancas == 0

  pior = casas.rindex do |casa|
    doces[casa -1] < criancas
  end

  casas.delete_at(pior) if pior

  casas
end