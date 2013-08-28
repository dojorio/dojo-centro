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
      busca(telefones, "1").should be_empty
    end

    it "joao se busca inclui telefone do joao" do
      telefones = {
        :joao => '21334455'
      }
      busca(telefones, "1").should == [:joao]
    end

    it "9 nao encontra ninguem" do
      telefones = {
        :joao => '21334455'
      }
      busca(telefones, "9").should == []
    end

    it "1 encontra o jose" do
      telefones = {
        :joao => '99999999',
        :jose => '19999999'
      }
      busca(telefones, "1").should == [:jose]
    end

    it "1 encontra o jose e o joao" do
      telefones = {
        :joao => '91999999',
        :jose => '19999999'
      }
      busca(telefones, "1").should == [:jose, :joao]
    end

    it "11 encontra o joao" do
      telefones = {
        :joao => '11999999',
        :jose => '19999999'
      }
      busca(telefones, "11").should == [:joao]
    end

    it "2 encontra o joao" do
      telefones = {
        :joao => '11999999',
        :jose => '19999999'
      }
      busca(telefones, "2").should == [:joao]
    end
  end
end
