# encoding: utf-8
require "./color_board.rb"

describe "Color board" do
    context "deve tratar jogada sem adjacências" do
        it "caso 1" do
            color_board([[1, 2, 3]], 0, 0).should == [[1, 2, 3]]
        end
        it "caso 2" do
            color_board([[3, 2, 1]], 0, 0).should == [[3, 2, 1]]
        end

        it "caso 3" do
            color_board([[4, 3, 2, 1]], 0, 0).should == [[4, 3, 2, 1]]
        end
        
        it "4 colunas clicando onde não há adjacência" do
            color_board([[4, 3, 2, 2]], 0, 1).should == [[4, 3, 2, 2]]
        end
    end
    
    context "deve tratar adjacências horizontal à direita" do
    
        it "caso 1" do
            color_board([[2, 1, 1]], 0, 1).should == [[2,nil,nil]]
        end

        it "caso 2" do
            color_board([[1, 2, 2]], 0, 1).should == [[1,nil,nil]]
        end

        it "caso 3" do
            color_board([[2, 2, 2]], 0, 1).should == [[nil,nil,nil]]
        end
        
        it "caso 4" do
            color_board([[3, 3, 3]], 0, 1).should == [[nil,nil,nil]]
        end
        
        it "4 colunas" do
            color_board([[4, 3, 2, 2]], 0, 2).should == [[4, 3, nil, nil]]
        end
        
        it "4 colunas novamente" do
            color_board([[4, 3, 2, 2]], 0, 3).should == [[4, 3, nil, nil]]
        end

        it "4 colunas novamente com 2 células adjacentes" do
            color_board([[2, 3, 2, 2]], 0, 3).should == [[2, 3, nil, nil]]
        end
        
        it "3 células adjacentes" do
            color_board([[2, 3, 2, 2, 2]], 0, 2).should == [[2, 3, nil, nil, nil]]
        end
        
    end
end

   
 
 