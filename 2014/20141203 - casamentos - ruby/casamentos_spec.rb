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

  it "um solteiro 21 anos nenhuma solteira" do
    solteiros = [21]
    solteiras = []
    expect(casamentos(solteiros, solteiras)).to eq([1, 21])
  end

  it "dois solteiro 21 anos nenhuma solteira" do
    solteiros = [21, 21]
    solteiras = []
    expect(casamentos(solteiros, solteiras)).to eq([2, 21])
  end

  it "dois solteiro 21 20 anos nenhuma solteira" do
    solteiros = [21, 20]
    solteiras = []
    expect(casamentos(solteiros, solteiras)).to eq([2, 20])
  end

  it "dois solteiro 21 20 anos, uma solteira" do
    solteiros = [21, 20]
    solteiras = [21]
    expect(casamentos(solteiros, solteiras)).to eq([1, 20])
  end
end