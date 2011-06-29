# encoding: utf-8

def onde_podem_mijar(mictorios)
    posicoes = []
    for i in (0..mictorios.length-1)
        anterior_vazio = (mictorios[i-1] != 1 or i == 0)
        atual_vazio = (mictorios[i] != 1)
        proximo_vazio = (mictorios[i+1] != 1 or i == mictorios.length - 1)
        
        if (anterior_vazio and atual_vazio and proximo_vazio)
            posicoes << i
            mictorios[i] = 1
        end
    end
    return posicoes
end

describe "onde_podem_mijar" do
    
    it "deve retornar [] se o unico lugar estiver ocupado" do
        mictorios = [1]
        onde_podem_mijar(mictorios).should == []
    end
    
    it "deve retornar [0] se o unico estiver vazio" do
        mictorios = [0]
        onde_podem_mijar(mictorios).should == [0]
    end
    
    it "deve retornar [0] se os dois (de dois) lugares estiverem vazios" do
        mictorios = [0, 0]
        onde_podem_mijar(mictorios).should == [0]
    end
    
    it "deve retornar [] se o primeiro lugar (de dois lugares) lugares estiver ocupado" do
        mictorios = [1, 0]
        onde_podem_mijar(mictorios).should == []
    end
    
    it "deve retornar [] se o segundo lugar (de dois lugares) estiver ocupado" do
        mictorios = [0, 1]
        onde_podem_mijar(mictorios).should == []
    end
    
    
    it "deve retornar [0,2] se os tres lugares estiverem vazios" do
        mictorios = [0, 0, 0]
        onde_podem_mijar(mictorios).should == [0,2]
    end
        
    it "deve retornar [0] se para [0,0,0,1,0,1,0,0,1]" do
        mictorios = [0,0,0,1,0,1,0,0,1]
        onde_podem_mijar(mictorios).should == [0]
    end
        
    it "deve retornar [0,2,4,6,8] para [0,0,0,0,0,0,0,0,0]" do
        mictorios = [0,0,0,0,0,0,0,0,0]
        onde_podem_mijar(mictorios).should == [0,2,4,6,8]
    end 
        
    it "deve retornar [2,4,6,8] para [1,0,0,0,0,0,0,0,0]" do
        mictorios = [1,0,0,0,0,0,0,0,0]
        onde_podem_mijar(mictorios).should == [2,4,6,8]
    end 
        
    it "deve retornar [3,5,7] para [1,1,0,0,0,0,0,0,0]" do
        mictorios = [1,1,0,0,0,0,0,0,0]
        onde_podem_mijar(mictorios).should == [3,5,7]
    end  
        
    it "deve retornar [4,6,8] para [1,0,1,0,0,0,0,0,0]" do
        mictorios = [1,0,1,0,0,0,0,0,0]
        onde_podem_mijar(mictorios).should == [4,6,8]
    end    
end

   
 
 