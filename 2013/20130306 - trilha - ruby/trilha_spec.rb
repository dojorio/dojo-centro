require "trilha"

describe "Trilha" do

  it "vazia" do
    distancias = []
    trilha(distancias, 1).should eq(0)
  end

  context "em um dia" do
    it "e com dois acampamentos" do
      distancias = [2]
      trilha(distancias, 1).should eq(2)
    end

    it "e com três acampamentos" do
      distancias = [2, 3]
      trilha(distancias, 1).should eq(5)
    end

    it "e com quatro acampamentos" do
      distancias = [2, 3, 4]
      trilha(distancias, 1).should eq(9)
    end
  end


  context "em dois dias" do
    it "e com dois acampamentos" do
      trilha([2], 2).should eq(2)
    end

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

    it "e com quatro acampamentos II" do
      trilha([3, 4, 1], 2).should eq(5)
    end

    it "e com quatro acampamentos III" do
      trilha([3, 4, 2], 2).should eq(6)
    end

    it "e com quatro acampamentos III invertido" do
      trilha([2, 4, 3], 2).should eq(6)
    end

    it "e com cinco acampamentos" do
      trilha([3, 2, 2, 3], 2).should eq(5)
    end

    it "e com cinco acampamentos II" do
      trilha([4, 2, 2, 4], 2).should eq(6)
    end

    it "e com cinco acampamentos III" do
      trilha([1, 1, 1, 4], 2).should eq(4)
    end

    it "e com cinco acampamentos IV" do
      trilha([1, 1, 1, 9], 2).should eq(9)
    end

    it "e com cinco acampamentos V" do
      trilha([1, 1, 1, 5], 2).should eq(5)
    end

    it "e com cinco acampamentos V invertido" do
      trilha([5, 1, 1, 1], 2).should eq(5)
    end

    it "e com cinco acampamentos VI" do
      trilha([1, 5, 1, 1], 2).should eq(6)
    end
  end

  context "em três dias" do
    it "e com cinco acampamentos" do
      trilha([1, 5, 1, 1], 3).should eq(5)
    end

    it "e com cinco acampamentos II" do
      trilha([1, 6, 1, 1], 3).should eq(6)
    end

    it "e com cinco acampamentos III" do
      trilha([1, 1, 6, 1], 3).should eq(6)
    end

    it "e com seis acampamentos" do
      trilha([1, 1, 2, 2, 1], 3).should eq(3)
    end
  end
end
