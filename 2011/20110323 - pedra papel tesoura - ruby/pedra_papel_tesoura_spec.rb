require "pedra_papel_tesoura"

describe Jokenpo do
    describe "deveria marcar como empate" do
        it "papel e papel" do
            jokenpo = Jokenpo.new("papel", "papel")
            jokenpo.resultado.should == "empate"
        end

        it "tesoura e tesoura" do
            jokenpo = Jokenpo.new("tesoura", "tesoura")
            jokenpo.resultado.should == "empate"
        end

        it "pedra e pedra" do
            jokenpo = Jokenpo.new("pedra", "pedra")
            jokenpo.resultado.should == "empate"
        end
    end
    describe "deveria marcar como tesoura" do
        it "papel e tesoura" do
            jokenpo = Jokenpo.new("papel", "tesoura")
            jokenpo.resultado.should == "tesoura"
        end
        
        it "tesoura e papel" do
            jokenpo = Jokenpo.new("tesoura", "papel")
            jokenpo.resultado.should == "tesoura"
        end
    end  
    describe "deveria marcar como pedra para" do
        it "tesoura e pedra" do
            jokenpo = Jokenpo.new("tesoura", "pedra")
            jokenpo.resultado.should == "pedra"
        end
        
        it "pedra e tesoura" do
            jokenpo = Jokenpo.new("pedra", "tesoura")
            jokenpo.resultado.should == "pedra"
        end    
    end
    describe "deveria papel como papel para" do
        it "pedra e papel" do
            jokenpo = Jokenpo.new("pedra", "papel")
            jokenpo.resultado.should == "papel"
        end
        
        it "papel e pedra" do
            jokenpo = Jokenpo.new("papel", "pedra")
            jokenpo.resultado.should == "papel"
        end
    end 
end

