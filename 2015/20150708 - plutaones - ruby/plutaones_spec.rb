require './plutaones'

describe "Plutaones" do
  it "converts 'a'" do
    expect('a'.to_plu).to eq('apla')
  end

  it "converts 'e'" do
    expect('e'.to_plu).to eq('eple')
  end

  it "converts 'i'" do
    expect('i'.to_plu).to eq('ipli')
  end

  it "converts 'ba'" do
    expect('ba'.to_plu).to eq('bapla')
  end

  it "converts 'bi'" do
    expect('bi'.to_plu).to eq('bipli')
  end

  it "converts 'aa'" do
    expect('aa'.to_plu).to eq('aplaapla')
  end

  it "converts 'abacaxi'" do
    expect('abacaxi'.to_plu).to eq('aplabaplacaplaxipli')
  end

  it "converts 'bens'" do
    expect('bens'.to_plu).to eq('beplenspls')
  end

  it "converts 'pó'" do
    expect('pó'.to_plu).to eq('pópló')
  end

  it "converts 'pó de mico'" do
    expect('pó de mico'.to_plu).to eq('pó deple miplicoplo')
  end

  it "converts 'bens materiais'" do
    expect('bens materiais'.to_plu).to eq('beplens maplatepleripliaplaiplispls')
  end
end