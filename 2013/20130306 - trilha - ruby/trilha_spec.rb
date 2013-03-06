require "trilha"

describe "Trilha" do
  it "vazia" do
    distancias = []
    trilha(distancias, 1).should eq(0)
  end

  it "em uma dia e com dois acampamentos" do
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

  it "em dois dias e com três acampamentos diferentes" do
    distancias = [2, 4]
    trilha(distancias, 2).should eq(4)
  end
end
