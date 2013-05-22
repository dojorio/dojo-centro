require "caixas"

describe Caixas do

  describe ".empilhar" do

    it "Com uma caixa" do
      caixas = [{ :peso => 1, :capacidade => 2 }]
      Caixas.empilhar(caixas).should == 1
    end

    it "Com duas caixas iguais empilhaveis" do
      caixas = [{ :peso => 1, :capacidade => 2 },
                { :peso => 1, :capacidade => 2 }]
      Caixas.empilhar(caixas).should == 2
    end

    it "Com duas caixas nao empilhaveis" do
      caixas = [{ :peso => 1, :capacidade => 0 },
                { :peso => 1, :capacidade => 0 }]
      Caixas.empilhar(caixas).should == 1
    end

    it "Com duas caixas empilhaveis" do
      caixas = [{ :peso => 1, :capacidade => 1 },
                { :peso => 1, :capacidade => 0 }]
      Caixas.empilhar(caixas).should == 2
    end
  end

end
