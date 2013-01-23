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

    it "de 11 deve ser onze" do
      extenso(11).should == "onze"
    end

    it "de 10 a 19 deve estar certo menos 11" do
      extenso(10).should == "dez"
      extenso(12).should == "doze"
      extenso(13).should == "treze"
      extenso(14).should == "quatorze"
      extenso(15).should == "quinze"
      extenso(16).should == "dezesseis"
      extenso(17).should == "dezessete"
      extenso(18).should == "dezoito"
      extenso(19).should == "dezenove"
    end

    it "de 20 a 90 (dezenas) deve estar certo" do
      extenso(20).should == "vinte"
      extenso(30).should == "trinta"
      extenso(40).should == "quarenta"
      extenso(50).should == "cinquenta"
      extenso(60).should == "sessenta"
      extenso(70).should == "setenta"
      extenso(80).should == "oitenta"
      extenso(90).should == "noventa"
    end

  end

end