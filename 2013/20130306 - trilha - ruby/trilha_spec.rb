require "trilha"

describe "Trilha" do
  it "vazia" do
    distancias = []
    trilha(distancias, 1).should eq(0)
  end

  it "uma parada" do
    distancias = [2]
    trilha(distancias, 1).should eq(2)
  end
end
