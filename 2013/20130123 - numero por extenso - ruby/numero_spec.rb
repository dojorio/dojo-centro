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

  end

end