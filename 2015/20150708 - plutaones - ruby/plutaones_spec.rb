require './plutaones'

describe "Plutaones" do
  it "converts 'a'" do
    expect('a'.to_plu).to eq('apla')
  end

  it "converts 'e'" do
    expect('e'.to_plu).to eq('eple')
  end
end