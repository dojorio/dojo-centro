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
  end
end
