require './telefone'

describe "Telefone" do
  it "is 1 for 1" do
    expect(telefone_de('1')).to eq('1')
  end

  it "is 0 for 0" do
    expect(telefone_de('0')).to eq('0')
  end

  it "is 2 for A" do
    expect(telefone_de('A')).to eq('2')
  end

  it "is 2 for B" do
    expect(telefone_de('B')).to eq('2')
  end

  it "is 2 for C" do
    expect(telefone_de('C')).to eq('2')
  end

  it "is 3 for D" do
    expect(telefone_de('D')).to eq('3')
  end

  it "is 3 for E" do
    expect(telefone_de('E')).to eq('3')
  end

  it "is 3 for F" do
    expect(telefone_de('F')).to eq('3')
  end

  it "is 4 for G" do
    expect(telefone_de('G')).to eq('4')
  end

  it "is 4 for H" do
    expect(telefone_de('H')).to eq('4')
  end

  it "is 4 for I" do
    expect(telefone_de('I')).to eq('4')
  end

  it "is 5 for J" do
    expect(telefone_de('J')).to eq('5')
  end

  it "is 5 for K" do
    expect(telefone_de('K')).to eq('5')
  end

  it "is 5 for L" do
    expect(telefone_de('L')).to eq('5')
  end

  it "is 6 for M" do
    expect(telefone_de('M')).to eq('6')
  end

  it "is 6 for N" do
    expect(telefone_de('N')).to eq('6')
  end

  it "is 6 for O" do
    expect(telefone_de('O')).to eq('6')
  end

  it "is 7 for P" do
    expect(telefone_de('P')).to eq('7')
  end

  it "is 7 for Q" do
    expect(telefone_de('Q')).to eq('7')
  end

  it "is 7 for R" do
    expect(telefone_de('R')).to eq('7')
  end

  it "is 7 for S" do
    expect(telefone_de('S')).to eq('7')
  end

  it "is 8 for T" do
    expect(telefone_de('T')).to eq('8')
  end

  it "is 8 for U" do
    expect(telefone_de('U')).to eq('8')
  end

  it "is 8 for V" do
    expect(telefone_de('V')).to eq('8')
  end

  it "is 9 for W" do
    expect(telefone_de('W')).to eq('9')
  end

  it "is 9 for X" do
    expect(telefone_de('X')).to eq('9')
  end

  it "is 9 for Y" do
    expect(telefone_de('Y')).to eq('9')
  end

  it "is 9 for Z" do
    expect(telefone_de('Z')).to eq('9')
  end

  it "is - for -" do
    expect(telefone_de('-')).to eq('-')
  end

  it "is 22 for AB" do
    expect(telefone_de('AB')).to eq('22')
  end

  it "is 22 for BA" do
    expect(telefone_de('BA')).to eq('22')
  end

  it "is 33 for DE" do
    expect(telefone_de('DE')).to eq('33')
  end

  it "is 33 for ED" do
    expect(telefone_de('ED')).to eq('33')
  end

  it "is 23 for AD" do
    expect(telefone_de('AD')).to eq('23')
  end

end
