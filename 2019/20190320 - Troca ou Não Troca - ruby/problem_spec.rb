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

  it "3 prêmios, 2 sim, 3 não" do
    rodadas = [[2, 1], [3, 0]]
    expect(troca_ou_nao(rodadas)).to eq(1)
  end

  it "3 prêmios, 3 sim, 2 sim" do
    rodadas = [[3, 1], [2, 1]]
    expect(troca_ou_nao(rodadas)).to eq(1)
  end

  it "3 prêmios, 3 não, 2 sim" do
    rodadas = [[3, 0], [2, 1]]
    expect(troca_ou_nao(rodadas)).to eq(2)
  end

  it "4 prêmios, 2 sim, 3 sim, 4 sim" do
    rodadas = [[2, 1], [3, 1], [4, 1]]
    expect(troca_ou_nao(rodadas)).to eq(0)
  end

  it "4 prêmios, 4 sim, 2 não, 3 sim" do
    rodadas = [[4, 1], [2, 0], [3, 1]]
    expect(troca_ou_nao(rodadas)).to eq(1)
  end

  it "4 prêmios, 4 sim, 2 sim, 3 sim" do
    rodadas = [[4, 1], [2, 1], [3, 1]]
    expect(troca_ou_nao(rodadas)).to eq(2)
  end
end
