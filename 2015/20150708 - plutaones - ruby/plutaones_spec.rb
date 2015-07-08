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

end