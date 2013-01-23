require "numero"

describe "Numero" do

  describe "inteiro por extenso" do
  
    it "de 1 deve ser um" do
      extenso(1).should == "um"
    end

    it "de 2 deve ser dois" do
      extenso(2).should == "dois"
    end
  
    it "de 3 deve ser três" do
      extenso(3).should == "três"
    end

    it "de 4 a 9 deve estar certo" do
      extenso(4).should == "quatro"
      extenso(5).should == "cinco"
      extenso(6).should == "seis"
      extenso(7).should == "sete"
      extenso(8).should == "oito"
      extenso(9).should == "nove"
    end
  end

end