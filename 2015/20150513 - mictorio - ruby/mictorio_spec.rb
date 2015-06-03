require './mictorio'

describe "Mictorio" do
  it "todos os 5 mictorios vazios 5" do
    expect(mictorios('00000')).to eq(5)
  end

  it "todos os mictorios vazios 7" do
    expect(mictorios('0000000')).to eq(7)
  end

  it "todos os mictorios ocupados" do
    expect(mictorios('11111')).to eq(0)
  end

  it "apenas um mictorio ocupado na ponta" do
    expect(mictorios('10000')).to eq(3)
  end

  it "apenas um mictorio ocupado no meio" do
    expect(mictorios('01000')).to eq(2)
  end

  it "apenas um mictorio ocupado na outra ponta" do
    expect(mictorios('00001')).to eq(3)
  end

  it "apenas um mictorio ocupado na ponta com mais mictorios" do
    expect(mictorios('100000')).to eq(4)
  end

  it "apenas um mictorio ocupado no meio com mais mictorios" do
    expect(mictorios('010000')).to eq(3)
  end

  it "apenas um mictorio ocupado no penultimo lugar" do
    expect(mictorios('000010')).to eq(3)
  end

  it "dois mictorios ocupados e nenhum vago" do
    expect(mictorios('10010')).to eq(0)
  end

  it "pessoas nas duas pontas" do
    expect(mictorios('1000101')).to eq(1)
  end

end