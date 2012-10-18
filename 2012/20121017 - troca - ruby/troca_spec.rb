require "troca"

describe "Troca" do
    let(:tabela){Tabela.new()}
    
    context "quando 1 abacate" do
        it "equivale a 2 laranjas" do
            tabela.defina(1, :abacate, 2, :laranja)
            
            tabela.troca(:laranja, :abacate).should == [2, 1]
        end
        
        it "equivale a 3 laranjas" do
            tabela.defina(1, :abacate, 3, :laranja)
            
            tabela.troca(:laranja, :abacate).should == [3, 1]
        end
    end
    
    context "quando 2 abacates" do
        it "equivalem a 1 laranja" do
            tabela.defina(2, :abacate, 1, :laranja)
            
            tabela.troca(:laranja, :abacate).should == [1, 2]
            tabela.troca(:abacate, :laranja).should == [2, 1]
        end

        it "equivalem a 3 laranjas" do
            tabela.defina(2, :abacate, 3, :laranja)
            
            tabela.troca(:laranja, :abacate).should == [3, 2]
            tabela.troca(:abacate, :laranja).should == [2, 3]
        end

        it "equivalem a 2 laranjas" do
            tabela.defina(2, :abacate, 2, :laranja)
            
            tabela.troca(:laranja, :abacate).should == [1, 1]
            tabela.troca(:abacate, :laranja).should == [1, 1]
        end
        
        context "equivalem a 3 laranjas" do            
            it "e 1 laranja equivale a 2 uvas" do
                tabela.defina(2, :abacate, 3, :laranja)
                tabela.defina(1, :laranja, 2, :uva)
                
                tabela.troca(:abacate, :uva).should == [1, 3]
                tabela.troca(:uva, :abacate).should == [3, 1]                
            end
        end
    end
end
