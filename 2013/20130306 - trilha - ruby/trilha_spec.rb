require "trilha"

describe "Trilha" do
  it "vazia" do
    distancias = []
    trilha(distancias, 1).should eq(0)
  end

  describe "em um dia" do
    it "e com dois acampamentos" do
      distancias = [2]
      trilha(distancias, 1).should eq(2)
    end

    it "e com três acampamentos" do
      distancias = [2, 3]
      trilha(distancias, 1).should eq(5)
    end
  end


  describe "em dois dias" do
    it "e com três acampamentos" do
      distancias = [2, 3]
      trilha(distancias, 2).should eq(3)
    end

    it "e com três acampamentos II" do
      distancias = [2, 4]
      trilha(distancias, 2).should eq(4)
    end

    it "e com quatro acampamentos" do
      trilha([2, 4, 1], 2).should eq(5)
    end

  end
end
