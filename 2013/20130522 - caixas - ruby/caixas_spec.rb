# -*- coding: utf-8 -*-

require "caixas"

describe Caixas do

  describe ".empilhar" do

    subject { Caixas.empilhar(caixas) }

    context "Com uma caixa" do
      let(:caixas) { [{ :peso => 1, :capacidade => 2 }] }
      it { should == 1 }
    end

    context "Com duas caixas iguais empilháveis" do
      let(:caixas) {[{ :peso => 1, :capacidade => 2 },
                     { :peso => 1, :capacidade => 2 }] }
      it { should == 2 }
    end

    context "Com duas caixas não empilháveis" do
      let(:caixas) {[{ :peso => 1, :capacidade => 0 },
                     { :peso => 1, :capacidade => 0 }] }
      it { should == 1 }
    end

    context "Com duas caixas empilháveis" do
      let(:caixas) {[{ :peso => 1, :capacidade => 1 },
                     { :peso => 1, :capacidade => 0 }] }
      it { should == 2 }
    end

    context "Com duas caixas não empilháveis com capacidade maior que 0" do
      let(:caixas) {[{ :peso => 2, :capacidade => 1 },
                     { :peso => 2, :capacidade => 1 }] }
      it { should == 1 }
    end

    context "Sem caixas" do
      let(:caixas) { [] }
      it { should == 0 }
    end

    context "Com 3 caixas empilhaveis" do
      let(:caixas) {[{ :peso => 2, :capacidade => 10 },
                     { :peso => 2, :capacidade => 10 },
                     { :peso => 2, :capacidade => 10 }] }
      it { should == 3 }
    end

    context "Com 3 caixas, 2 empilhaveis" do
      let(:caixas) {[{ :peso => 2, :capacidade => 10 },
                     { :peso => 2, :capacidade => 10 },
                     { :peso => 11, :capacidade => 10 }] }
      it { should == 2 }
    end

    context "Com 3 caixas, nenhuma empilhavel" do
      let(:caixas) {[{ :peso => 11, :capacidade => 10 },
                     { :peso => 11, :capacidade => 10 },
                     { :peso => 11, :capacidade => 10 }] }
      it { should == 1 }
    end

    context "Com 3 caixas, dois empilhaveis de novo" do
      let(:caixas) {[{ :peso => 15, :capacidade => 0 },
                     { :peso => 5,  :capacidade => 15 },
                     { :peso => 10, :capacidade => 19 }] }
      it { should == 2 }
    end

    context "Com 4 caixas, escolher a 3 melhor" do
      let(:caixas) {[{ :peso => 1, :capacidade => 1 },
                     { :peso => 1,  :capacidade => 2 },
                     { :peso => 4,  :capacidade => 3 },
                     { :peso => 4, :capacidade => 4 }] }
      it { should == 3 }
    end

  end

end
