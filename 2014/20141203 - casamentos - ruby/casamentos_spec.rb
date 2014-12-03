require './casamentos'

describe "Casamentos" do
  context "um solteiro uma solteira" do
    let(:solteiros) { [20] }
    let(:solteiras) { [20] }
    it { expect(casamentos(solteiros, solteiras)).to eq([0]) }
    it { expect(casais(solteiros, solteiras)).to eq([[20, 20]]) }
  end

  context "um solteiro nenhuma solteira" do
    let(:solteiros) { [20] }
    let(:solteiras) { [] }
    it { expect(casamentos(solteiros, solteiras)).to eq([1, 20]) }
    it { expect(casais(solteiros, solteiras)).to eq([]) }
  end

  context "um solteiro 21 anos nenhuma solteira" do
    let(:solteiros) { [21] }
    let(:solteiras) { [] }
    it { expect(casamentos(solteiros, solteiras)).to eq([1, 21]) }
    it { expect(casais(solteiros, solteiras)).to eq([]) }
  end

  context "dois solteiro 21 anos nenhuma solteira" do
    let(:solteiros) { [21, 21] }
    let(:solteiras) { [] }
    it { expect(casamentos(solteiros, solteiras)).to eq([2, 21]) }
    it { expect(casais(solteiros, solteiras)).to eq([]) }
  end

  context "dois solteiro 21 20 anos nenhuma solteira" do
    let(:solteiros) { [21, 20] }
    let(:solteiras) { [] }
    it { expect(casamentos(solteiros, solteiras)).to eq([2, 20]) }
    it { expect(casais(solteiros, solteiras)).to eq([]) }
  end

  context "dois solteiro 21 20 anos, uma solteira" do
    let(:solteiros) { [21,  20] }
    let(:solteiras) { [21] }
    it { expect(casamentos(solteiros, solteiras)).to eq([1, 20]) }
    it { expect(casais(solteiros, solteiras)).to eq([[21, 21]]) }
  end

  context "dois solteiro 21 22 anos, uma solteira" do
    let(:solteiros) { [21, 22] }
    let(:solteiras) { [21] }
    it { expect(casamentos(solteiros, solteiras)).to eq([1, 21]) }
    it { expect(casais(solteiros, solteiras)).to eq([[22, 21]]) }
  end

  context "tres solteiro 21 22 30 anos, uma solteira" do
    let(:solteiros) { [21, 22,30] }
    let(:solteiras) { [21] }
    it { expect(casamentos(solteiros, solteiras)).to eq([2, 21]) }
    it { expect(casais(solteiros, solteiras)).to eq([[30, 21]]) }
  end

  context "um solteiro 21 anos, dois solteira" do
    let(:solteiros) { [21] }
    let(:solteiras) { [21, 15] }
    it { expect(casamentos(solteiros, solteiras)).to eq([0]) }
    it { expect(casais(solteiros, solteiras)).to eq([[21, 21]]) }
  end

  context "cinco solteiro 21, 22, 23, 24, 25 anos, dois solteira" do
    let(:solteiros) { [21, 22, 23, 25, 25] }
    let(:solteiras) { [21, 22] }
    it { expect(casamentos(solteiros, solteiras)).to eq([3, 21]) }
    it { expect(casais(solteiros, solteiras)).to eq([[25, 22], [25, 21]]) }
  end

  it "um homem tres mulheres" do
    solteiros = [20]
    solteiras = [15, 21, 30]
    expect(casais(solteiros, solteiras)).to eq([[20,21]])
  end
end