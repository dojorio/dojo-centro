require './celular'

describe "Celular" do
  it "escreve 'A'" do
    expect(escrever("A")).to eq("2")
  end

  it "escreve 'D'" do
    expect(escrever("D")).to eq("3")
  end
  
  it "escreve 'G'" do
    expect(escrever("G")).to eq("4")
  end

  it "escreve 'J'" do
    expect(escrever("J")).to eq("5")
  end

  it "escreve 'B" do
    expect(escrever("B")).to eq("22")
  end

  it "escreve 'AE" do
    expect(escrever("AE")).to eq("233")
  end

  it "escreve 'SEMPRE" do
    expect(escrever("SEMPRE")).to eq("77773367_77733")
  end
 
  it "escreve frase inteira" do
    expect(escrever( "SEMPRE ACESSO O DOJOPUZZLES")).to eq("77773367_7773302_222337777_777766606660366656667889999_9999555337777")
  end
end