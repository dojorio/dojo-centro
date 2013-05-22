# -*- coding: utf-8 -*-

require "caixas"

describe Caixas do

  describe ".empilhar" do

    it "Com uma caixa" do
      caixas = [{ :peso => 1, :capacidade => 2 }]
      Caixas.empilhar(caixas).should == 1
    end

    it "Com duas caixas iguais empilháveis" do
      caixas = [{ :peso => 1, :capacidade => 2 },
                { :peso => 1, :capacidade => 2 }]
      Caixas.empilhar(caixas).should == 2
    end

    it "Com duas caixas não empilháveis" do
      caixas = [{ :peso => 1, :capacidade => 0 },
                { :peso => 1, :capacidade => 0 }]
      Caixas.empilhar(caixas).should == 1
    end

    it "Com duas caixas empilháveis" do
      caixas = [{ :peso => 1, :capacidade => 1 },
                { :peso => 1, :capacidade => 0 }]
      Caixas.empilhar(caixas).should == 2
    end

    it "Com duas caixas não empilháveis com capacidade maior que 0" do
      caixas = [{ :peso => 2, :capacidade => 1 },
                { :peso => 2, :capacidade => 1 }]
      Caixas.empilhar(caixas).should == 1
    end

    it "Sem caixas" do
      caixas = []
      Caixas.empilhar(caixas).should == 0
    end

    it "Com 3 caixas empilhaveis" do
      caixas = [{ :peso => 2, :capacidade => 10 },
                { :peso => 2, :capacidade => 10 },
                { :peso => 2, :capacidade => 10 }]
      Caixas.empilhar(caixas).should == 3
    end

    it "Com 3 caixas, 2 empilhaveis" do
      caixas = [{ :peso => 2, :capacidade => 10 },
                { :peso => 2, :capacidade => 10 },
                { :peso => 11, :capacidade => 10 }]
      Caixas.empilhar(caixas).should == 2
    end
  end

end
