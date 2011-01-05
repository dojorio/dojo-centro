require "espiral"

describe Espiral do
  describe "quando tem 1 linha" do
    it "deve retornar 1 ao receber 1,1" do
      espiral = Espiral.new(1, 1)
      espiral.linha(1).should == [1]
    end

    it "deve retonar 1,2 ao receber 1,2" do
      espiral = Espiral.new(1, 2)
      espiral.linha(1).should == [1,2]
    end

    it "deve retonar 1..3 ao receber 1,3" do
      espiral = Espiral.new(1, 3)
      espiral.linha(1).should == [1, 2, 3]
    end

    it "deve retonar 1..4 ao receber 1,4" do
      espiral = Espiral.new(1, 4)
      espiral.linha(1).should == [1, 2, 3, 4]
    end
  end

  describe "quando tem 1 coluna" do
    it "deve retonar 1,2 ao receber 2, 1" do
      espiral = Espiral.new(2, 1)
      espiral.coluna(1).should == [1, 2]
    end
    it "deve retonar 1..3 ao receber 3, 1" do
      espiral = Espiral.new(3, 1)
      espiral.coluna(1).should == [1, 2, 3]
    end
  end

  describe "quando recebe 2 linhas e 2 colunas" do

      it "deve ter a primeira linha 1,2" do
      espiral = Espiral.new(2,2)
      espiral.linha(1).should == [1,2]
    end

    it "deve ter a segunda linha 4,3" do
      espiral = Espiral.new(2,2)
      espiral.linha(2).should == [4,3]
    end
  end

  describe "quando tem 2 linhas e 3 colunas" do
    before do
       @espiral = Espiral.new(2,3)
    end
    it "deve ter a primeira linha 1,2,3" do
      @espiral.linha(1).should == [1,2,3]
    end

    it "deve ter a segunda linha 6,5,4" do
      @espiral.linha(2).should == [6,5,4]
    end

    it "deve ter a segunda coluna 2,5" do
      @espiral.coluna(2).should == [2,5]
    end

    it "deve ter a terceira coluna 3,4" do
      @espiral.coluna(3).should == [3,4]
    end
  end

  describe "quando tem 3 linhas e 3 colunas" do
    it "deve ter a primeira linha 1,2,3" do
      espiral = Espiral.new(3,3)
      espiral.linha(1).should == [1,2,3]

    end
    it "deve ter a segunda linha 6,5,4" do
      espiral = Espiral.new(2,3)
      espiral.linha(2).should == [6,5,4]
    end
  end




end

