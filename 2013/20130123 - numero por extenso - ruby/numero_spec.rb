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

    it "de 21 deve ser vinte e um" do
      extenso(21).should == "vinte e um"
    end

    it "de 22 deve ser vinte e dois" do
      extenso(22).should == "vinte e dois"
    end

    it "de 31 deve ser trinta e um" do
      extenso(31).should == "trinta e um"
    end

    it "de 42 deve ser quarenta e dois" do
      extenso(42).should == "quarenta e dois"
    end

    it "de 99 deve ser noventa e nove" do
      extenso(99).should == "noventa e nove"
    end

    it "de 100 deve ser cem" do
      extenso(100).should == "cem"
    end

    it "de centenas deve estar certo" do
      extenso(200).should == "duzentos"
      extenso(300).should == "trezentos"
      extenso(400).should == "quatrocentos"
      extenso(500).should == "quinhentos"
      extenso(600).should == "seiscentos"
      extenso(700).should == "setecentos"
      extenso(800).should == "oitocentos"
      extenso(900).should == "novecentos"
    end

    it "de 101 deve ser cento e um" do
      extenso(101).should == "cento e um"
    end
  end

end