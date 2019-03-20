require_relative 'problem'

describe "Troca ou Não Troca" do
  it "2 prêmios, sim" do
    rodadas = [[2, 1]]
    expect(troca_ou_nao(rodadas)).to eq(0)
  end

  it "2 prêmios, não" do
    rodadas = [[2, 0]]
    expect(troca_ou_nao(rodadas)).to eq(1)
  end

  it "3 prêmios, 3 sim, 2 não" do
    rodadas = [[3, 1], [2, 0]]
    expect(troca_ou_nao(rodadas)).to eq(0)
  end
end
