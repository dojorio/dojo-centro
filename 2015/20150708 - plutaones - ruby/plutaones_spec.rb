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


end