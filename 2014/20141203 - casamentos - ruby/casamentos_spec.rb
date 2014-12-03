require './casamentos'

describe "Casamentos" do
  it "um solteiro uma solteira" do
    solteiros = [20]
    solteiras = [20]
    expect(casamentos(solteiros, solteiras)).to eq([0])
  end

  it "um solteiro nenhuma solteira" do
    solteiros = [20]
    solteiras = []
    expect(casamentos(solteiros, solteiras)).to eq([1, 20])
  end
end