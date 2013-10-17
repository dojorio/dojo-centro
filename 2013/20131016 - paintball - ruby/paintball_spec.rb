# -*- coding: utf-8 -*-
require './paintball.rb'

describe "Paintball" do
  it "quadrado degenerado" do
    paintball(0, 0, [], []).should be_false 
  end

  it "quadrado de area 1" do
    paintball(1, 1, [1], []).should eq 1
  end
  it "outro quadrado de area 1" do
    paintball(1, 1, [], [1]).should eq 1
  end

  it "outro quadrado de area 1 sem bola" do
    paintball(1, 1, [], []).should be_false
  end 

  it "quadrado maior que tinta disponivel" do
    paintball(2, 2, [1], []).should be_false
  end

  it "quadrado maior que tinta disponivel" do
    paintball(1.5, 1.5, [1], []).should be_false
  end

  it "quadrado certinho" do
    paintball(Math.sqrt(2), Math.sqrt(2), [1], []).should eq 1
  end

  it "retângulo 1x2" do
    paintball(1, 2, [], [Math.sqrt(5)/2]).should eq 1
  end

  it "retângulo 1x2 bolas raio 1" do
    paintball(1, 2, [1, 1], [1, 1]).should eq 2
  end
end
