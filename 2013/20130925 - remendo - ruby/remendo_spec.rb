# -*- coding: utf-8 -*-
require './remendo.rb'

describe "Remendo" do
  it "para nenhum furo" do
    furos = []
    expect(remendo(furos, 20, 2, 3)).to eq 0
  end

  context "para um furo" do
    let(:furos) { [10] }

    it "com r1 < r2" do
      expect(remendo(furos, 20, 2, 3)).to eq 2
    end

    it "com r1 > r2"  do
      expect(remendo(furos, 20, 3, 2)).to eq 2
    end
  end

  context "para dois furos" do
    
    it "proximos" do
      furos = [10, 11]
      expect(remendo(furos, 20, 2, 3)).to eq 2
    end

    it "afastados" do
      furos = [10, 13]
      expect(remendo(furos, 20, 2, 3)).to eq 3
    end

    it "afastados com maior remendo maior que a distancia entre os furos" do
      furos = [10, 13]
      expect(remendo(furos, 20, 2, 4)).to eq 4
    end

    it "mais afastados que o maior remendo" do
      furos = [10, 15]
      expect(remendo(furos, 20, 3, 4)).to eq 6
    end

    it "proximos dando a volta" do
      furos = [1, 19]
      expect(remendo(furos, 20, 2, 3)).to eq 2
    end

    it "afastados dando a volta" do
      furos = [2, 19]
      expect(remendo(furos, 20, 2, 3)).to eq 3
    end

    it "afastados onde é melhor usar duas emendas" do
      furos = [10, 13]
      expect(remendo(furos, 20, 1, 3)).to eq 2
    end
  end

  context "para três furos" do
    it "proximos" do
      furos = [10, 11, 14]
      expect(remendo(furos, 20, 3, 4)).to eq 4
    end

    it "proximos com 2 na ponta" do
      furos = [10, 14, 15]
      expect(remendo(furos, 20, 3, 4)).to eq 6
    end

    it "proximos com 2 na outra ponta" do
      furos = [10, 11, 15]
      expect(remendo(furos, 20, 3, 4)).to eq 6
    end

    it "proximos com 2 ponta mas sendo melhor usar um remendo grande" do
      furos = [10, 14, 20]
      expect(remendo(furos, 20, 3, 4)).to eq 7
    end

    it "com dois furos retro-próximos" do
      furos = [1, 14, 19]
      expect(remendo(furos, 20, 3, 4)).to eq 6
    end



  end

end
