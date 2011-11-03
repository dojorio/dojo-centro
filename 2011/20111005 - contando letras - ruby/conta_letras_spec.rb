# encoding: utf-8
require "./conta_letras.rb"

casos = [2, 6, 10, 16, 21, 25]

describe "dado um contador" do
    it "deve indicar soma para todos os numeros ate 20" do
        (1..casos.size).each { |i|
        contar(i).should == casos[i-1] }
    end
end

describe "número de letras em número por extenso" do
    it "funciona para 7 a 13" do
        respostas = [4, 4, 4, 3, 4, 4, 5]
        (7..13).each { |i|
            numero_letras(i).should == respostas[i-7]
        }
    end
    
    it "funcionar para o 21" do
        numero_letras(21).should == 8
    end
    
    it "funcionar para o 22" do
        numero_letras(22).should == 10
    end
    
    it "funciona para 23 a 29" do
        respostas = {
            23 => 6 + 4,
            24 => 6 + 6,
            25 => 6 + 5,
            26 => 6 + 4,
            27 => 6 + 4,
            28 => 6 + 4,
            29 => 6 + 4,
        }
        (23..29).each { |i|
            numero_letras(i).should == respostas[i]
        }
    end
    
    it "funciona para 30" do
       numero_letras(30).should == 6
    end
    
end




   
 
 