require "trilha"

describe "Trilha" do
  it "vazia" do
    distancias = []
    trilha(distancias, 1).should eq(0)
  end

  it "com uma parada" do
    distancias = [2]
    trilha(distancias, 1).should eq(2)
  end

  it "em uma dia e com três acampamentos" do
    distancias = [2, 3]
    trilha(distancias, 1).should eq(5)
  end

  it "em dois dias e com três acampamentos" do
    distancias = [2, 3]
    trilha(distancias, 2).should eq(3)
  end
end
