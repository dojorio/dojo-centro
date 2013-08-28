require './telefone.rb'

describe "Telefone" do
  context "busca pelo número" do
    it "ninguem se nao houver busca" do
      telefones = {}
      busca(telefones, "").should be_empty
    end

    it "joao se busca for vazia" do
      telefones = {
        :joao => '22334455'
      }
      busca(telefones, "").should == [:joao]
    end

    it "ninguem se busca nao inclui joao" do
      telefones = {
        :joao => '22334455'
      }
      busca(telefones, "1").should == []
    end

    it "joao se busca inclui telefone do joao" do
      telefones = {
        :joao => '21334455'
      }
      busca(telefones, "1").should == [:joao]
    end
  end
end
