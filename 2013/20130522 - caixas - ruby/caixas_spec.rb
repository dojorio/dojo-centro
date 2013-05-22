require "caixas"

describe Caixas do

  describe ".empilhar" do

    context "uma caixa" do

      it "deve ser sempre 1" do
        caixas = [{ :peso => 1, :capacidade => 2 }]
        Caixas.empilhar(caixas).should == 1
      end

    end

  end

end
