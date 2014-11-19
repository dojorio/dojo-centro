def halloween(criancas, doces)
  casas = (1..doces.length).to_a
  total_doces = doces.reduce(:+)

  return casas if total_doces % criancas == 0

  carlos = []
  doces.each_with_index do |qtd_doces, i|
    carlos << i + 1 if qtd_doces / criancas > 0
  end
  carlos

end