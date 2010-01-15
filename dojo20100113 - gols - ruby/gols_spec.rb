require 'gols'

describe "Saldo de Gols" do

	it "deve retornar o saldo de gols igual a 2 de uma partida que foi 7 a 5" do
        
        partida = [7, 5]
        
        saldo = calc_saldo partida
        
        saldo.should ==  2
 	end
    
    it "deve retornar o saldo de gols igual a 3 de uma partida que foi 5 a 2" do
        
        partida = [5, 2]
        
        saldo = calc_saldo partida
        
        saldo.should ==  3
 	end
 
    it "deve receber uma lista com uma partida de uma equipe e retornar o indice um duas vezes " do
        
        partidas = [1,
                    [7,5],
                    0
                   ]
        
        saldos = lista_saldos partidas
        
        saldos.should == [1,
                         [1,1]]
    end
 
    it "deve fornecer uma lista com uma partida de uma equipe e retornar nenhum" do
        
        partidas = [1,
                    [5,7],
                    0
                   ]
        
        saldos = lista_saldos partidas
        
        saldos.should == [1,'nenhum']
    end
    
    it "deve receber uma lista com um empate de uma equipe e retornar nenhum" do
        partidas = [1,
                    [2,2],
                    0
                   ]
        saldos = lista_saldos partidas
        saldos.should == [1,'nenhum']
    end
    
    it "deve receber uma lista de partidas com resultadosde uma equipe e retornar a melhor partida" do
        partidas = [2,
                    [1,2],
                    [2,1],
                    0
                   ]
        saldos = lista_saldos partidas
        saldos.should == [1,[2,2]]
    end
    
end
