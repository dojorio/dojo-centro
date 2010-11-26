require 'spec'
require 'espiral'

describe "espiral" do
  describe "com uma linha" do
    it "e uma coluna" do
      gera_espiral(1, 1).should == '1'
    end

    it "e duas colunas" do
      gera_espiral(1, 2).should == '1 2'
    end

    it "e três colunas" do
      gera_espiral(1, 3).should == '1 2 3'
    end
  end

  describe "com uma coluna" do
    it "e duas linhas" do
      gera_espiral(2, 1).should == "1\n2"
    end

    it "e três linhas" do
      gera_espiral(3, 1).should == "1\n2\n3"
    end
  end

  it "com duas linhas e duas colunas" do
    gera_espiral(2, 2).should == "1 2\n4 3"
  end


end

